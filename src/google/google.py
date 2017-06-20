import argparse
import os
import time
import datetime
import json

import googleapiclient.discovery
from six.moves import input
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
from oauth2client.client import AccessTokenCredentials
from urllib import urlencode
from urllib2 import Request , urlopen, HTTPError



class Google:

    def __init__(self, google_client_id, google_client_secret, google_refresh_token):
        auth_request = Request('https://accounts.google.com/o/oauth2/token',
                  data=urlencode({
                    'grant_type': 'refresh_token',
                    'client_id': google_client_id,
                    'client_secret': google_client_secret,
                    'refresh_token': google_refresh_token }),
                  headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json' })
        auth_response = json.load(urlopen(auth_request))
        google_access_token= auth_response['access_token']
        google_credentials = AccessTokenCredentials(google_access_token, "MyAgent/1.0", None)
        self.GOOGLE_METRIC_NAME = "custom.cloudmonitoring.googleapis.com/pid"
        self.google_monitor_client = googleapiclient.discovery.build('cloudmonitoring', 'v2beta2', credentials=google_credentials)

        self.compute = build('compute', 'v1', credentials=google_credentials)

    def operation_wait(self, project_id, google_zone, operation_name):
        while True:
            compute_result = self.compute.zoneOperations().get(
                project=project_id,
                zone=google_zone,
                operation=operation_name).execute()

            if compute_result['status'] == 'DONE':
                if 'error' in compute_result:
                    raise Exception(compute_result['error'])
                return compute_result

            time.sleep(1)

    def create_instance(self, project_id, zone, instance_name, bucket_name ):
        image_result = self.compute.images().getFromFamily(
            project='debian-cloud', family='debian-8').execute()
        disk_image = image_result['selfLink']
        machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
        google_startup_script = open(
            os.path.join(
                os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
        google_image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
        google_image_caption = "Ready for test!"

        config = {
            'name': instance_name,
            'machineType': machine_type,
            'disks': [
                {
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                        'sourceImage': disk_image,
                    }
                }
            ],
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [
                    {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
                ]
            }],
            'serviceAccounts': [{
                'email': 'default',
                'scopes': [
                    'https://www.googleapis.com/auth/devstorage.read_write',
                    'https://www.googleapis.com/auth/logging.write'
                ]
            }],
            'metadata': {
                'items': [{
                    'key': 'startup-script',
                    'value': google_startup_script
                }, {
                    'key': 'url',
                    'value': google_image_url
                }, {
                    'key': 'text',
                    'value': google_image_caption
                }, {
                    'key': 'bucket',
                    'value': bucket_name
                }]
            }
        }

        operation= self.compute.instances().insert(
            project=project_id,
            zone=zone,
            body=config).execute()

        self.operation_wait(project_id, zone, operation['name'])

    def list_instances(self, project_id, zone):
        compute_result = self.compute.instances().list(project=project_id, zone=zone).execute()
        google_instances = compute_result['items']
        instance_list = []
        for google_instance in google_instances:
            instance_list.append(google_instance['name'])
        return instance_list


    def delete_instance(self, project_id, zone, instance_name):
        operation = self.compute.instances().delete(project=project_id, zone=zone, instance=instance_name).execute()
        self.operation_wait(project_id, zone, operation['name'])


    def format_rfc3339(self, datetime_instance=None):
        return datetime_instance.isoformat ("T") + "Z"

    def get_now_rfc3339(self):
        return self.format_rfc3339 (datetime.datetime.utcnow ())

    def cloud_monitor(self, project_id):
        self.google_client = googleapiclient.discovery.build ('cloudmonitoring', 'v2beta2')
        set_now = self.get_now_rfc3339 ()
        description = {"project": project_id,
                "metric": self.GOOGLE_METRIC_NAME}
        point = {"start": set_now,
                 "end": set_now,
                 "doubleValue": os.getpid ()}
        try:
            write_request = self.google_monitor_client.timeseries ().write (
                project=project_id,
                body={"timeseries": [{"timeseriesDesc": description, "point": point}]})
            write_request.execute ()  
        except Exception as e:
            raise

        read_request = self.google_monitor_client.timeseries ().list (
            project=project_id,
            metric=self.GOOGLE_METRIC_NAME,
            youngest=set_now)
        start = time.time ()
        while True:
            try:
                read_response = read_request.execute ()
                for point in read_response["timeseries"][0]["points"]:
                    print("Point:  {}: {}".format (
                        point["end"], point["doubleValue"]))
                break
            except Exception as e:
                if time.time () < start + 20:
                    print("Failed to read custom metric data, retrying...")
                    time.sleep (3)
                else:
                    print("Failed to read custom metric data, aborting: "
                          "exception={}".format (e))
                    raise

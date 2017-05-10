import argparse
import os
import time
import datetime
import json

# import googleapiclient.discovery
# from six.moves import input
# from oauth2client.client import GoogleCredentials
# from googleapiclient.discovery import build
# from oauth2client.client import AccessTokenCredentials
# from urllib import urlencode
# from urllib2 import Request , urlopen, HTTPError



class Google:

    # def __init__(self, google_client_id, google_client_secret, google_refresh_token):
    #     auth_request = Request('https://accounts.google.com/o/oauth2/token',
    #               data=urlencode({
    #                 'grant_type': 'refresh_token',
    #                 'client_id': google_client_id,
    #                 'client_secret': google_client_secret,
    #                 'refresh_token': google_refresh_token }),
    #               headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json' })
    #     auth_response = json.load(urlopen(auth_request))
    #     google_access_token= auth_response['access_token']
    #     google_credentials = AccessTokenCredentials(google_access_token, "MyAgent/1.0", None)
    #     self.compute = build('compute', 'v1', credentials=google_credentials)

    def operation_wait(self, project_id, google_zone, operation_name):
        print('Waiting for operation to finish...')
        while True:
            compute_result = self.compute.zoneOperations().get(
                project=project_id,
                zone=google_zone,
                operation=operation_name).execute()

            if compute_result['status'] == 'DONE':
                print("done.")
                if 'error' in compute_result:
                    raise Exception(compute_result['error'])
                return compute_result

            time.sleep(1)

    def create_instance(self, project_id, zone, instance_name, bucket_name ):

        print('********************************Creating instance*********************************')
        print project_id, zone, instance_name, bucket_name
        # getting latest debian-8 image.
        # image_result = self.compute.images().getFromFamily(
        #     project='debian-cloud', family='debian-8').execute()
        # disk_image = image_result['selfLink']

        # # Configuring the virtual machine with machine type, startup script, and image configurations.
        # machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
        # google_startup_script = open(
        #     os.path.join(
        #         os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
        # google_image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
        # google_image_caption = "Ready for test!"

        # config = {
        #     'name': instance_name,
        #     'machineType': machine_type,

        #     # Configuring boot disk.
        #     'disks': [
        #         {
        #             'boot': True,
        #             'autoDelete': True,
        #             'initializeParams': {
        #                 'sourceImage': disk_image,
        #             }
        #         }
        #     ],

        #     # COnfiguring network interface
        #     'networkInterfaces': [{
        #         'network': 'global/networks/default',
        #         'accessConfigs': [
        #             {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
        #         ]
        #     }],

        #     # COnfiguring scope.
        #     'serviceAccounts': [{
        #         'email': 'default',
        #         'scopes': [
        #             'https://www.googleapis.com/auth/devstorage.read_write',
        #             'https://www.googleapis.com/auth/logging.write'
        #         ]
        #     }],

        #     # configuring metadata
        #     'metadata': {
        #         'items': [{
        #             'key': 'startup-script',
        #             'value': google_startup_script
        #         }, {
        #             'key': 'url',
        #             'value': google_image_url
        #         }, {
        #             'key': 'text',
        #             'value': google_image_caption
        #         }, {
        #             'key': 'bucket',
        #             'value': bucket_name
        #         }]
        #     }
        # }

        # operation= self.compute.instances().insert(
        #     project=project_id,
        #     zone=zone,
        #     body=config).execute()

        # self.operation_wait(project_id, zone, operation['name'])
###############

    def list_instances(self, project_id, zone):
        print "*******************************************list_instances*********************************************"
        print project_id, zone
        # compute_result = self.compute.instances().list(project=project_id, zone=zone).execute()
        # google_instances = compute_result['items']
        # print('Instances in project %s and zone %s:' % (project_id, zone))
        # for google_instance in google_instances:
        #     print(' - ' + google_instance['name'])


    def delete_instance(self, project_id, zone, instance_name):

        print'*******************************************Deleting instance*******************************************'
        # operation = self.compute.instances().delete(project=project_id, zone=zone, instance=instance_name).execute()
        # self.operation_wait(project_id, zone, operation['name'])


    def format_rfc3339(self, datetime_instance=None):
        return datetime_instance.isoformat ("T") + "Z"

    def get_now_rfc3339(self):
        return self.format_rfc3339 (datetime.datetime.utcnow ())
 #
 #    def cloud_monitor(self, project_id):
 #        print "****************************************cloud monitor*************************************************"
 # ##################
 #        GOOGLE_METRIC_NAME = "custom.cloudmonitoring.googleapis.com/pid"
 #        google_client = googleapiclient.discovery.build ('cloudmonitoring', 'v2beta2')
 #        set_now = self.get_now_rfc3339 ()
 #        description = {"project": project_id,
 #                "metric": GOOGLE_METRIC_NAME}
 #        point = {"start": set_now,
 #                 "end": set_now,
 #                 "doubleValue": os.getpid ()}
 #        print("Writing {} at {}".format (point["doubleValue"], set_now))
 #
 #        # Write a new data point.
 #        try:
 #            write_request = google_client.timeseries ().write (
 #                project=project_id,
 #                body={"timeseries": [{"timeseriesDesc": description, "point": point}]})
 #            write_request.execute ()  # Ignore the response.
 #        except Exception as e:
 #            print("Failed to write custom metric data: exception={}".format (e))
 #            raise
 #
 #        print("Reading data from custom metric timeseries...")
 #        read_request = google_client.timeseries ().list (
 #            project=project_id,
 #            metric=GOOGLE_METRIC_NAME,
 #            youngest=set_now)
 #        start = time.time ()
 #        while True:
 #            try:
 #                read_response = read_request.execute ()
 #                for point in read_response["timeseries"][0]["points"]:
 #                    print("Point:  {}: {}".format (
 #                        point["end"], point["doubleValue"]))
 #                break
 #            except Exception as e:
 #                if time.time () < start + 20:
 #                    print("Failed to read custom metric data, retrying...")
 #                    time.sleep (3)
 #                else:
 #                    print("Failed to read custom metric data, aborting: "
 #                          "exception={}".format (e))
 #                    raise
######################
    #
    # Point:  2017 - 05 - 01
    # T05:17:23.000
    # Z: 43495.0
    # Point:  2017 - 05 - 01
    # T05:12:10.000
    # Z: 40906.0

if __name__ == '__main__':
    gc= Google("32555940559.apps.googleusercontent.com", "ZmssLNjJy2998hD4CTg2ejr2", "1/Czt1brCXjU5UzTRfVrE4OUmHUL9RfUHRHd-K1HelXPo")
    gc.list_instances("autum-165318", "us-central1-f")
    # gc.set_pid("autum-165318")
    # gc.set_bucket_name("autum")
    # gc.set_zone("us-central1-f")
    # gc.set_instance_name("autumtest2")
    gc.create_instance("autum-165318","us-central1-f","autumtest-2","autum2" )
    # gc.delete_instance("autum-165318", "us-central1-f", "autumtest2")
    # gc.cloud_monitor("autum-165318")

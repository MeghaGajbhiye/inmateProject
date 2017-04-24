import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()


class Google:

    def wait_for_operation(self, compute, project, zone, operation):
        print('Waiting for operation to finish...')
        while True:
            result = compute.zoneOperations().get(
                project=project,
                zone=zone,
                operation=operation).execute()

            if result['status'] == 'DONE':
                print("done.")
                if 'error' in result:
                    raise Exception(result['error'])
                return result

            time.sleep(1)

    def create_instance(self, project_id, zone, instance_name, bucket_name ):

        print('Creating instance.')
        # Get the latest Debian Jessie image.
        compute = googleapiclient.discovery.build('compute', 'v1')
        image_response = compute.images().getFromFamily(
            project='debian-cloud', family='debian-8').execute()
        source_disk_image = image_response['selfLink']

        # Configure the machine
        machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
        startup_script = open(
            os.path.join(
                os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
        image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
        image_caption = "Ready for dessert?"

        config = {
            'name': instance_name,
            'machineType': machine_type,

            # Specify the boot disk and the image to use as a source.
            'disks': [
                {
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                        'sourceImage': source_disk_image,
                    }
                }
            ],

            # Specify a network interface with NAT to access the public
            # internet.
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [
                    {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
                ]
            }],

            # Allow the instance to access cloud storage and logging.
            'serviceAccounts': [{
                'email': 'default',
                'scopes': [
                    'https://www.googleapis.com/auth/devstorage.read_write',
                    'https://www.googleapis.com/auth/logging.write'
                ]
            }],

            # Metadata is readable from the instance and allows you to
            # pass configuration from deployment scripts to instances.
            'metadata': {
                'items': [{
                    # Startup script is automatically executed by the
                    # instance upon startup.
                    'key': 'startup-script',
                    'value': startup_script
                }, {
                    'key': 'url',
                    'value': image_url
                }, {
                    'key': 'text',
                    'value': image_caption
                }, {
                    'key': 'bucket',
                    'value': bucket_name
                }]
            }
        }

        operation= compute.instances().insert(
            project=project_id,
            zone=zone,
            body=config).execute()

        self.wait_for_operation(compute, project_id, zone, operation['name'])

        print("""
           Instance created.
           It will take a minute or two for the instance to complete work.
           """)


    def list_instances(self, project_id, zone):
        compute = googleapiclient.discovery.build('compute', 'v1')
        result = compute.instances().list(project=project_id, zone=zone).execute()
        instances = result['items']
        print('Instances in project %s and zone %s:' % (project_id, zone))
        for instance in instances:
            print(' - ' + instance['name'])


    def delete_instance(self, project_id, zone, instance_name):

        print('Deleting instance.')
        compute = googleapiclient.discovery.build('compute', 'v1')

        # operation = self.delete_instance(compute, self.get_project_id(), self.get_zone(), self.get_instance_name())

        operation = compute.instances().delete(project=project_id, zone=zone, instance=instance_name).execute()
        self.wait_for_operation(compute, project_id, zone, operation['name'])

        print("""  Instance Deleted.
                   It will take a minute or two for the instance to be deleted.
                   """)



if __name__ == '__main__':
    gc= Google()
    # gc.set_pid("autum-165318")
    # gc.set_bucket_name("autum")
    # gc.set_zone("us-central1-f")
    # gc.set_instance_name("autumtest3")
    gc.create_instance("autum-165318","us-central1-f","autumtest-1","autum" )
    # gc.delete_instance("autum-165318", "us-central1-f", "autumtest1")

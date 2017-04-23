import pyrax

class Rackspace:

    def __init__(self, userName, apiKey, instance_name, ram, image_name):
        self.user_name = userName
        self.api_key = apiKey
        self.ram = ram
        self.image_name = image_name
        self.instance_name = instance_name

    def get_user_name(self):
        return self.user_name

    def get_api_key(self):
        return self.api_key

    def get_ram(self):
        self.ram = 1024
        return self.ram

    def get_image_name(self):
        self.image_name = 'Debian 7 (Wheezy) (PVHVM)'
        return self.image_name

    def get_instance_name(self):
        return self.instance_name

    def describe_flavor(self, cs):
        '''Listing the flavor of servers'''
        flavor_list = cs.list_flavors()
        for f in flavor_list:
            print "Name:", f.name
            print "  ID:", f.id
            print "  RAM:", f.ram
            print "  Disk:", f.disk
            print "  VCPUs:", f.vcpus
        flavor_1GB = [flavor for flavor in cs.flavors.list() if flavor.ram == self.get_ram()][0]
        return flavor_1GB.id

    # NOw let us get image and flavor to choose the image and hardware config for the server
    #image = pyrax.images.get('2919d767-668d-47ad-aa01-5f55f37d6d47')


    def launch_instance(self):
        '''Create Server'''
        pyrax.set_setting('identity_type', 'rackspace')
        pyrax.set_credentials(username=self.get_user_name(), api_key=self.get_api_key())
        cs = pyrax.cloudservers
        images = pyrax.images.list()
        for img in images:
            if img.name==self.get_image_name():
                imagetest = img.id
                return imagetest

        server = cs.servers.create(self.instance_name, imagetest, self.describe_flavor(images))
        # End result: Server created in Rackspace


    def delete_instance(self):
        '''delete instance'''
        for server in cs.servers.list():
            server.delete()


if __name__ =="__main__":
    r = Rackspace("", "", "test5", 1024, "Debian 7 (Wheezy) (PVHVM)")
    r.launch_instance()

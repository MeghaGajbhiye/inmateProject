import pyrax

class Rackspace:

    def __init__(self, userName, apiKey):
        self.user_name = userName
        self.api_key = apiKey
        pyrax.set_setting('identity_type', 'rackspace')
        pyrax.set_credentials(username=self.user_name, api_key=self.api_key)
        self.cs = pyrax.cloudservers

    def launch_instance(self,instance_name ,image_name, ram):
        '''Create Server'''
        images = pyrax.images.list()
        #image_name = 'Debian 7 (Wheezy) (PVHVM)'
        for img in images:
            if img.name == image_name:
                image_test = img.id

        server = self.cs.servers.create(instance_name, image_test, self.describe_flavor(ram))
        print server.id
        # End result: Server created in Rackspace


    def describe_flavor(self, ram):
        '''Listing the flavor of servers'''
        #ram = 1024
        flavor_list = self.cs.list_flavors()
        # for f in flavor_list:
        #     print "Name:", f.name
        #     print "  ID:", f.id
        #     print "  RAM:", f.ram
        #     print "  Disk:", f.disk
        #     print "  VCPUs:", f.vcpus
        flavor = [flavor for flavor in self.cs.flavors.list() if flavor.ram == ram][0]
        return flavor.id

    def view_instances(self):
        print "inside view instances"
        server = self.cs.servers.list()
        server_name = []
        server_ip = []
        if server is not None:
            print "inside not none"
            for servers in server:
                server_name.append(servers.name)
                # server_ip.append(servers.data)
            print server_ip
            return server_name
        else:
            print "none"
            return 1

    def update_instance(self, server_name, ram):
        server = self.cs.servers.list()
        # print server
        for servers in server:
            print servers.name
            if servers.name == server_name:
                server_id = servers.id
                server = self.cs.servers.get(server_id)
                flavor_id = self.describe_flavor(ram)
                server.resize(flavor_id)
                return 1
            else:
                return 0

    def delete_instance(self, server_name):
        for server in self.cs.servers.list():
            if server.name == server_name:
                server.delete()
                return 1
        return 0

    def monitoring(self, ipAddress, host):
        cm = pyrax.cloud_monitoring

        # To list the available check types
        chk_types = cm.list_check_types ()
        for checktypes in chk_types:
            print checktypes

        # lists all the monitoring zones
        monitoring_zones = cm.list_monitoring_zones ()
        for MonitoringZones in monitoring_zones:
            print MonitoringZones

        # to Crete email notifications.
        email = cm.create_notification ("email", label="my_email_notification",
                                        details={"address": "megha.gajbhiye@sjsu.edu"})
        # To create entity. We need input of the sevres ip address and host. host can be http://ipaddress.

        ent = cm.create_entity (name="sample_entity123", ip_addresses={"example": ipAddress},
                                metadata={"description": "Just a test entity"})
        chk = cm.create_check (ent, label="sample_check", check_type="remote.http", details={"url": host}, period=900,
                               timeout=20, monitoring_zones_poll=["mzdfw", "mzlon", "mzsyd"], target_hostname=host)

        print chk

if __name__ =="__main__":
    r = Rackspace("achal126", "9ac58056270b4447a6154662d160ef9f")
    sn = r.view_instances()
    # print sn
    # r.launch_instance("test2", "Debian 7 (Wheezy) (PVHVM)", 1024)
    # print r.update_instance("test2", 2048)
    # result = r.delete_instance("test1")
    # print result
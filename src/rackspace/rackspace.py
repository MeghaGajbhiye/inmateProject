import pyrax


class Rackspace:
    def __init__(self, userName, apiKey):
        self.user_name = userName
        self.api_key = apiKey
        pyrax.set_setting ('identity_type', 'rackspace')
        pyrax.set_credentials (username=self.user_name, api_key=self.api_key)
        self.cs = pyrax.cloudservers

    def launch_instance(self, instance_name, image_name, ram):
        '''Create Server'''
        print "*************************INSIDE LAUNCH INSTANCE ****************************************"
        print self.user_name, self.api_key, instance_name, image_name, ram
        #################################################################################
        # images = pyrax.images.list ()
        # # image_name = 'Debian 7 (Wheezy) (PVHVM)'
        # for img in images:
        #     if img.name == image_name:
        #         image_test = img.id
        #
        # server = self.cs.servers.create (instance_name, image_test, self.describe_flavor (ram))
        # pyrax.utils.wait_until (server, "status", "ACTIVE", interval=1, attempts=30)
        # print server.id
        # End result: Server created in Rackspace
        #################################################################################

    def describe_flavor(self, ram):
        '''Listing the flavor of servers'''
        # ram = 1024
        flavor_list = self.cs.list_flavors ()
        # for f in flavor_list:
        #     print "Name:", f.name
        #     print "  ID:", f.id
        #     print "  RAM:", f.ram
        #     print "  Disk:", f.disk
        #     print "  VCPUs:", f.vcpus
        flavor = [flavor for flavor in self.cs.flavors.list () if flavor.ram == ram][0]
        return flavor.id

    def view_instances(self):

        print "*********************** VIEW INSTANCE **********************************************"
        print self.user_name, self.api_key

        ################################################################################
        print "inside view instances"
        server = self.cs.servers.list ()
        server_name = []
        server_ip = []
        if server is not None:
            print "inside not none"
            for servers in server:
                server_name.append (servers.name)
                server_ip.append (servers.accessIPv4)
            print server_ip
            return server_name
        else:
            print "none"
            return 1
        # #################################################################################

    def update_instance(self, server_name, ram):
        print "*****************************INside UPdate INstance*****************************************"
        print self.api_key, self.user_name, server_name, ram
        # #################################################################################
        # server = self.cs.servers.list ()
        # # print server
        # for servers in server:
        #     print servers.name
        #     if servers.name == server_name:
        #         server_id = servers.id
        #         server = self.cs.servers.get (server_id)
        #         flavor_id = self.describe_flavor (ram)
        #         server.resize (flavor_id)
        #         return 1
        #     else:
        #         return 0
        # ###################################################################################3

    def delete_instance(self, server_name):
        print "*************************************** INSIDE DELETE RACKSPACE ***********************"
        print self.user_name, self.api_key, server_name
        #################################################################################
        # for server in self.cs.servers.list ():
        #     if server.name == server_name:
        #         server.delete ()
        #         return 1
        # return 0
        #################################################################################
    def monitoring(self, instance_name, notification, email_id):
        print "*************************************** INSIDE MONITORING RACKSPACE ***********************"
        print self.user_name, self.api_key, instance_name, notification, email_id
        # #################################################################################
        # cm = pyrax.cloud_monitoring
        # lst_entities = cm.list_entities ()
        # for entity in lst_entities:
        #     print entity.id
        #     lst_alarms = cm.list_alarms (entity.id)  # this call seem to have some issue
        #     print lst_alarms
        #     break
        #
        # server = self.cs.servers.list ()
        # ipAddress = ''
        # if server is not None:
        #     for servers in server:
        #         if servers.name == instance_name:
        #             ipAddress = servers.accessIPv4
        #
        # host = "http://" + ipAddress
        # print instance_name
        # print ipAddress
        # print host
        #
        # # To list the available check types
        # chk_types = cm.list_check_types ()
        # # for checktypes in chk_types:
        # #     print checktypes
        #
        # # lists all the monitoring zones
        # monitoring_zones = cm.list_monitoring_zones ()
        # # for MonitoringZones in monitoring_zones:
        # #     print MonitoringZones
        #
        # # to Crete email notifications.
        # email = cm.create_notification ("email", label="my_email_notification",
        #                                 details={"address": "megha.gajbhiye@sjsu.edu"})
        # # To create entity. We need input of the sevres ip address and host. host can be http://ipaddress.
        #
        # ent = cm.create_entity (name="sample_entity123", ip_addresses={"example": ipAddress},
        #                         metadata={"description": "Just a test entity"})
        #
        # email = cm.create_notification ("email", label="my_email_notification",
        #                                 details={"address": email_id})
        # plan = cm.create_notification_plan (label="default", ok_state=email, warning_state=email,
        #                                     critical_state=email)
        #
        # if notification =="Duration":
        #     print "inside Duration"
        #     chk = cm.create_check (ent, label="check_duration", check_type="remote.http", details={"url": host}, period=900,
        #                            timeout=20, target_hostname=ipAddress)
        #     alarm = cm.create_alarm (ent, chk, plan,
        #                              "if (metric['duration'] > 2000) { return new AlarmStatus(WARNING); } return new AlarmStatus(OK);")
        #
        # if notification == "CPU":
        #     print "inside cpu"
        #     chk = cm.create_check (ent, label="check_cpu", check_type="agent.cpu", details={"url": host}, period=900,
        #                            timeout=20, target_hostname=ipAddress)
        #     alarm = cm.create_alarm (ent, chk, plan,
        #                              "if (rate(metric['usage_average']) > 10) { return new AlarmStatus(WARNING); } return new AlarmStatus(OK);")
        #
        # elif notification == "Memory":
        #     print "inside memory"
        #     chk = cm.create_check (ent, label="check_memory", check_type="agent.memory", details={"url": host},
        #                            period=900,
        #                            timeout=20, target_hostname=ipAddress)
        #     alarm = cm.create_alarm (ent, chk, plan,
        #                              "if (percentage(metric['actual_used'], metric['total']) > 90) { return new "
        #                              "AlarmStatus(WARNING); } return new AlarmStatus(OK);")
        #
        # elif notification == "Ping":
        #     print "Inside ping"
        #     chk = cm.create_check (ent, label="sample_check", check_type="remote.http", details={"url": host},
        #                            period=900,
        #                            timeout=20, monitoring_zones_poll=["mzdfw", "mzlon", "mzsyd"],
        #                            target_hostname=ipAddress)
        #     alarm = cm.create_alarm (ent, chk, plan,
        #                              "if (rate(metric['average']) > 10) { return new AlarmStatus(WARNING); } return "
        #                              "new AlarmStatus(OK);")
        #
        # elif notification == "5 minute load average":
        #     print "inside 5min load"
        #     chk = cm.create_check (ent, label="sample_check", check_type="agent.load_average", details={"url": host},
        #                            period=900,
        #                            timeout=20, monitoring_zones_poll=["mzdfw", "mzlon", "mzsyd"],
        #                            target_hostname=ipAddress)
        #     alarm = cm.create_alarm (ent, chk, plan,
        #                              "if (metric['5m'] > ${critical_threshold}) { return new AlarmStatus(WARNING); } "
        #                              "return new AlarmStatus(OK);")
        #
        # # print("Name:", ent.name)
        # # print("ID:", ent.id)
        # # print("IPs:", ent.ip_addresses)
        # # print("Meta:", ent.metadata)
        # # elif notification == "Memory":
        # # elif notification == "Ping":
        # #     alarm = cm.create_alarm (ent, chk, plan,
        # #                              "if (metric['duration'] > 2000) { return new AlarmStatus(WARNING); } return new AlarmStatus(OK);")
        #
        # # lst_entities = cm.list_entities ()
        # # chglogs = cm.get_changelogs (ent)
        # # print chglogs
        #
        # lst_alarms = cm.list_alarms (ent.id)
        # # print lst_alarms
        # #     break
        # # print chk.list_metrics
        # #################################################################################
    def instance_reboot(self, server_name, boot_type):
        print "*************************************** INSIDE REBOOT RACKSPACE ***********************"
        print self.user_name, self.api_key, server_name, boot_type
        # servers = self.cs.servers.list ()
        # # Find the first 'ACTIVE' server
        # try:
        #     active = [server for server in servers
        #               if server.status == "ACTIVE" and server.name == server_name][0]
        # except IndexError:
        #     print("There are no active servers in your account.")
        #     print("Please create one before running this script.")
        # # Display server info
        # print("Server Name:", active.name)
        # print("Server ID:", active.id)
        # print("Server Status:", active.status)
        # print()
        #
        # # servers = cs.servers.list()
        # # # Find the first 'ACTIVE' server
        # # try:
        # #     active = [server for server in servers
        # #             if server.status == "ACTIVE"][0]
        # # except IndexError:
        # #     print("There are no active servers in your account.")
        # #     print("Please create one before running this script.")
        # #     sys.exit()
        # # # Display server info
        # # print("Server Name:", active.name)
        # # print("Server ID:", active.id)
        # # print("Server Status:", active.status)
        # # print()
        #
        # answer = boot_type
        # reboot_type = {"s": "soft", "h": "hard"}[answer]
        # active.reboot (reboot_type)
        # # Reload the server
        # after_reboot = self.cs.servers.get (active.id)
        #
        # print("Server Status =", after_reboot.status)


if __name__ == "__main__":
    r = Rackspace ("achal126", "9ac58056270b4447a6154662d160ef9f")
    sn = r.view_instances()
    monitoring = r.monitoring ("instance_test", "Ping","megha.gajbhiye@sjsu.edu")
    # print sn
    # r.launch_instance("instance_test", "Debian 7 (Wheezy) (PVHVM)", 1024)
    # print r.update_instance("test2", 2048)
    # result = r.delete_instance("instance_test")
    # print result

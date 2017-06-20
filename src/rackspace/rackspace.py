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
        images = pyrax.images.list ()
        for img in images:
            if img.name == image_name:
                image_test = img.id

        print (image_test)

        server = self.cs.servers.create (instance_name, image_test, self.describe_flavor(ram))
        pyrax.utils.wait_until (server, "status", "ACTIVE", interval=1, attempts=30)
        
    def describe_flavor(self, ram):
        '''Listing the flavor of servers'''
        flavor = [flavor for flavor in self.cs.flavors.list () if flavor.ram == ram][0]
        return flavor.id

    def view_instances(self):

        server = self.cs.servers.list ()
        server_name = []
        server_ip = []
        if server is not None:
            for servers in server:
                server_name.append (servers.name)
                server_ip.append (servers.accessIPv4)
            return server_name
        else:
            return 1
        
    def update_instance(self, server_name, ram):
        server = self.cs.servers.list ()
        for servers in server:
            if servers.name == server_name:
                server_id = servers.id
                server = self.cs.servers.get (server_id)
                flavor_id = self.describe_flavor(ram)
                server.resize (flavor_id)
                return 1
            else:
                return 0
        
    def delete_instance(self, server_name):
        for server in self.cs.servers.list ():
            if server.name == server_name:
                print "server name", server_name
                server.delete ()
                return 1
        return 0
        
    def monitoring(self, instance_name, notification, email_id, entity_name):
        cm = pyrax.cloud_monitoring
        lst_entities = cm.list_entities ()
        for entity in lst_entities:
            lst_alarms = cm.list_alarms (entity.id)  
            break

        server = self.cs.servers.list ()
        ipAddress = ''
        if server is not None:
            for servers in server:
                if servers.name == instance_name:
                    ipAddress = servers.accessIPv4

        host = "http://" + ipAddress
        chk_types = cm.list_check_types ()
        monitoring_zones = cm.list_monitoring_zones ()
        email = cm.create_notification ("email", label="my_email_notification",
                                        details={"address": email_id})
        ent = cm.create_entity (name=entity_name, ip_addresses={"example": ipAddress},
                                metadata={"description": "Just a test entity"})

        email = cm.create_notification ("email", label="my_email_notification",
                                        details={"address": email_id})
        plan = cm.create_notification_plan (label="default", ok_state=email, warning_state=email,
                                            critical_state=email)

        if notification =="Duration":
            print "inside Duration"
            chk = cm.create_check (ent, label="check_duration", check_type="remote.http", details={"url": host}, period=900,
                                   timeout=20, target_hostname=ipAddress)
            alarm = cm.create_alarm (ent, chk, plan,
                                     "if (metric['duration'] > 2000) { return new AlarmStatus(WARNING); } return new AlarmStatus(OK);")

        if notification == "CPU":
            print "inside cpu"
            chk = cm.create_check (ent, label="check_cpu", check_type="agent.cpu", details={"url": host}, period=900,
                                   timeout=20, target_hostname=ipAddress)
            alarm = cm.create_alarm (ent, chk, plan,
                                     "if (rate(metric['usage_average']) > 10) { return new AlarmStatus(WARNING); } return new AlarmStatus(OK);")

        elif notification == "Memory":
            print "inside memory"
            chk = cm.create_check (ent, label="check_memory", check_type="agent.memory", details={"url": host},
                                   period=900,
                                   timeout=20, target_hostname=ipAddress)
            alarm = cm.create_alarm (ent, chk, plan,
                                     "if (percentage(metric['actual_used'], metric['total']) > 90) { return new "
                                     "AlarmStatus(WARNING); } return new AlarmStatus(OK);")

        elif notification == "Ping":
            print "Inside ping"
            chk = cm.create_check (ent, label="sample_check", check_type="remote.http", details={"url": host},
                                   period=900,
                                   timeout=20, monitoring_zones_poll=["mzdfw", "mzlon", "mzsyd"],
                                   target_hostname=ipAddress)
            alarm = cm.create_alarm (ent, chk, plan,
                                     "if (rate(metric['average']) > 10) { return new AlarmStatus(WARNING); } return "
                                     "new AlarmStatus(OK);")

        elif notification == "5 minute load average":
            print "inside 5min load"
            chk = cm.create_check (ent, label="sample_check", check_type="agent.load_average", details={"url": host},
                                   period=900,
                                   timeout=20, monitoring_zones_poll=["mzdfw", "mzlon", "mzsyd"],
                                   target_hostname=ipAddress)
            alarm = cm.create_alarm (ent, chk, plan,
                                     "if (metric['5m'] > ${critical_threshold}) { return new AlarmStatus(WARNING); } "
                                     "return new AlarmStatus(OK);")
        lst_alarms = cm.list_alarms (ent.id)

    def instance_reboot(self, server_name, boot_type):
        servers = self.cs.servers.list ()
        try:
            active = [server for server in servers
                      if server.status == "ACTIVE" and server.name == server_name][0]
        except IndexError:
            print("There are no active servers in your account.")
        answer = boot_type
        reboot_type = {"s": "soft", "h": "hard"}[answer]
        print "reboot_type %r" %reboot_type
        active.reboot(reboot_type)
        after_reboot = self.cs.servers.get (active.id)

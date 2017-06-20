import requests
import json


# http://docs.oracle.com/cloud/latest/stcomputecs/STCSG/GUID-433AEA3E-F569-45BB-8373-6108524EE25E.htm#OCSUG308
# https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/Authentication.html
#

# Authentication

class ORACLE:
    def __init__(self, name, password, domain_name):
        print "inside init of oracle"
        print "name ", name, "passowrd ", password, "domain_name ", domain_name
        self.name = name
        self.password = password
        self.domain_name = domain_name
        self.user = '/Compute-' + self.domain_name + "/" + self.name
        print self.user
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/authenticate/'
        self.data = {'user': self.user, 'password': self.password}
        self.header = {'Content-Type': 'application/oracle-compute-v3+json'}
        self.request = requests.post(self.url, data=json.dumps(self.data), headers=self.header)
        self.cookievalue = self.request.cookies.values()
        print self.cookievalue[0]
        print self.request.status_code
        self.mycookie = 'nimbula=' + self.cookievalue[0]

        # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-launchplan--post.html
        # Error resolution link: https://docs.oracle.com/cloud/latest/stcomputecs/STCSG/GUID-6F1C8BB6-EF64-4408-B504-ED94C1CE1B7E.htm#STCSG-GUID-6F1C8BB6-EF64-4408-B504-ED94C1CE1B7E

        # Create instance
    def create_instance(self, shape, image):
    	print "shape ", shape, "image", image
        print "inside create instance"

        self.url = 'https://api-z70.compute.us6.oraclecloud.com/launchplan/'
        self.data={"instances": [{"shape": shape, "imagelist": image}]}
        self.header={'Cookie': self.mycookie, 'Content-Type': 'application/oracle-compute-v3+json', 'Accept': 'application/oracle-compute-v3+json'}
        self.request=requests.post(self.url,data=json.dumps(self.data),headers=self.header)
        print self.request.text
        print self.request.status_code


        # Create ImageList

    def create_image_list(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist/Compute-' + self.domain_name + '/' + self.name + '/'
        print self.url
        print self.name
        self.header = {'Cookie': self.mycookie, 'Content-Type': 'application/oracle-compute-v3+json',
                       'Accept': 'application/oracle-compute-v3+json'}

        self.data = {
            "default": 2,
            "description": "ol 62",
            "name": "/Compute-" + self.domain_name+ "/" + self.name + "/ol 62"
        }
        self.request = requests.post(self.url, data=json.dumps(self.data), headers=self.header)
        print self.request.text
        print self.request.status_code

    # Details of all the Imagelists
    # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-imagelist-%7Bcontainer%7D--get.html

    # curl -X GET
    #      -H "Cookie: $COMPUTE_COOKIE"
    #      -H "Accept: application/oracle-compute-v3+json"
    #      https://api-z999.compute.us0.oraclecloud.com/imagelist/Compute-acme/jack.jones@example.com/


    def describe_instances(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist' + self.user
        self.header = {'Cookie': self.mycookie, 'Accept': 'application/oracle-compute-v3+json'}
        self.request = requests.get(self.url, headers=self.header)
        print self.request.text
        print self.request.status_code

    # Update Image List
    # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-imagelist-%7Bname%7D-put.html
    def update_instance(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist' + self.user
        self.header = {'Cookie': self.mycookie, 'Content-Type': 'application/oracle-compute-v3+json',
                       'Accept': 'application/oracle-compute-v3+json'}

        self.data = {
            "default": 2,
            "description": "OL 6.6 40 GB",
            "name": self.user + "/ol66_40GB"
        }

        self.request = requests.put(self.url, data=self.data, headers=self.header)
        print self.request.status_code
        print self.request.text

    # Delete imageList
    # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-imagelist-%7Bname%7D-delete.html
    def delete_instance(self, instanceid):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/instance/Compute-' + self.domain_name + '/' + self.name +'/' + instanceid
        self.header = {'Cookie': self.mycookie}
        self.request = requests.delete(self.url, headers=self.header)
        print self.request.status_code

    def insert_image_list(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist/' + self.user + '/ol6/entry/'
        self.header = {'Cookie': self.mycookie, 'Content-Type': 'application/oracle-compute-v3+json',
                       'Accept': 'application/oracle-compute-v3+json'}
        self.data = {
            "attributes": {"type": "Oracle Linux 6.6"},
            "version": 2,
            "machineimages": [self.user + "/ol66_40GB"],
        }
        self.request = requests.post(self.url, data=json.dumps(self.data), headers=self.header)
        print self.request.text
        print self.request.status_code

    # Delete an Image List Entry
    # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-imagelist-%7Bname%7D-entry-%7Bversion%7D-delete.html
    def delete_image_list(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist' + self.user
        self.header = {'Cookie': self.mycookie}
        self.request = requests.delete(self.url, headers=self.header)
        print self.request.text
        print self.request.status_code

    # Retrieve Details of an Image List Entry
    # https://docs.oracle.com/cloud/latest/stcomputecs/STCSA/op-imagelist-%7Bname%7D-entry-%7Bversion%7D-get.html
    def view_image_list(self):
        self.url = 'https://api-z70.compute.us6.oraclecloud.com/imagelist' + self.user
        self.header = {'Cookie': self.mycookie, 'Accept': 'application/oracle-compute-v3+json'}
        self.request = requests.get(self.url, headers=self.header)
        print self.request.text
        print self.request.status_code

if __name__ == "__main__":
    orc = ORACLE("ivar.iitg@gmail.com", "Seattle@2015", 'a499832')
    print "Check"
    orc.create_instance("oc3", "/oracle/public/OL_6.7_UEKR4_x86_64")
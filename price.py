from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = ''
EC2_SECRET_KEY = ''

cls = get_driver(Provider.EC2)
driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY)
sizes = driver.list_sizes()
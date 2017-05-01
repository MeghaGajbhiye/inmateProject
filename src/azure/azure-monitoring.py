# from azure.monitor import MonitorClient
# from azure.common.credentials import UserPassCredentials
# from azure.mgmt.resource.resources import ResourceManagementClient
# from azure.common.credentials import ServicePrincipalCredentials as spc
#
# subscription_id = '7197d513-b8a1-425e-9065-2cf1cb785455'
#
# # See above for details on creating different types of AAD credentials
# credentials = spc(
#             client_id="ad6f5554-f2ae-420d-af5d-831cdc7ce984",
#             secret=self.SECRET_KEY,
#             tenant=self.TENANT_ID
#         )
#
# resource_client = ResourceManagementClient(
#     credentials,
#     subscription_id
# )
#
# resource_client.providers.register('Microsoft.Insights')
# # Replace this with your subscription id
#
# client = MonitorClient(
#     credentials,
#     subscription_id
# )
#
# # import urllib2
# # response = urllib2.urlopen('https://management.azure.com/subscriptions/7197d513-b8a1-425e-9065-2cf1cb785455/resourceGroups/group1/providers/${resourceProviderNamespace}/${resourceType}/${resourceName}/providers/microsoft.insights/metrics?`$filter=${filter}&api-version=${apiVersion}')
# # print response.info()
# # html = response.read()
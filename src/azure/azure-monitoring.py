import urllib2
response = urllib2.urlopen('https://management.azure.com/subscriptions/7197d513-b8a1-425e-9065-2cf1cb785455/resourceGroups/group1/providers/${resourceProviderNamespace}/${resourceType}/${resourceName}/providers/microsoft.insights/metrics?`$filter=${filter}&api-version=${apiVersion}')
print response.info()
html = response.read()
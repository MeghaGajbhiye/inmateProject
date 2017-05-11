import json
import datetime

d = {
    'name': 'Foo'
}
print(json.dumps(d))  # {"name": "Foo"}
d['date'] = datetime.datetime.now()
# print(json.dumps(d))
d['date'] = datetime.datetime.now()


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


print(json.dumps(d, default=myconverter))

# import json
# json_output = {u'TerminatingInstances': [{u'InstanceId': 'i-0f8cd205ff577869e', u'CurrentState': {u'Code': 32, u'Name': 'shutting-down'}, u'PreviousState': {u'Code': 16, u'Name': 'running'}}], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '01c517cb-0baf-4dbf-b89a-614514b503ec', 'HTTPHeaders': {'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'server': 'AmazonEC2', 'content-type': 'text/xml;charset=UTF-8', 'date': 'Thu, 11 May 2017 00:25:03 GMT'}}}

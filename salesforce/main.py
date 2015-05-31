import beatbox
import datetime

service = beatbox.PythonClient()
service.serverUrl = 'https://test.salesforce.com/services/Soap/u/20.0'
service.login('username', 'password')

dt = datetime.datetime(2015, 5, 1, 8, 0, 0)

with open('/input/file/path', 'r') as input_file:
    object_ids = []
    for line in input_file:
        object_ids.append(line.strip())

output_file = open('/output/file/path', 'w')

object_name = 'Insertion_Order__c'

for object_id in object_ids:
    query_result = service.query('SELECT Id, \
                                         First_Live_Date__c \
                                  FROM {} \
                                  WHERE Id = \'{}\''.format(object_name, object_id))
    records = query_result['records']

    if not records:
        continue

    record = records[0]

    if record['First_Live_Date__c'] is None or record['First_Live_Date__c'] > dt:
        print record['Id'] + ' ' + str(record['First_Live_Date__c'])
        output_file.write(record['Id'] + ',2015-05-01T08:00:00Z\n')
    else:
        print '[OMIT] ' + record['Id'] + ' ' + str(record['First_Live_Date__c'])

output_file.close()

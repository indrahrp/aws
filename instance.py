import boto3,sys

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

import sys



ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)
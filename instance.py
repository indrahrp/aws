#!/bin/env python
import boto3,sys
INSTANCE_ID='i-0438130683c08f96b'
ec2 = boto3.resource('ec2')

#ec2 = boto3.client('ec2')
#response = ec2.describe_instances()
#print(response)

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)

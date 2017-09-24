#!/usr/bin/env python
import sys
import boto3
ec2 = boto3.resource('ec2')

#for instance_id in sys.argv[1:]:
for instance in ec2.instances.all():
    #instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response

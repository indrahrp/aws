#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-4fffc834',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Servername','Value':'ct-lin1'}]}],
    InstanceType='t2.micro')
print instance[0].id

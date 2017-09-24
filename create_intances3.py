#!/usr/bin/env python

import boto3,sys
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-4fffc834',
    MinCount=1,
    MaxCount=1, 
    #SubnetId='subnet-f9eb08b2',
    #NetworkInterfaces=[{'AssociatePublicIpAddress':True,'DeviceIndex':0,'PrivateIpAddress':'10.32.0.181'}],
    NetworkInterfaces=[{'DeviceIndex':0,'PrivateIpAddress':'10.32.0.181',    'SubnetId':'subnet-f9eb08b2'},
    {'DeviceIndex':1,'PrivateIpAddress':'10.32.1.181',    'SubnetId':'subnet-3924c672'}],
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Servername','Value': sys.argv[1]}]}],
    InstanceType='t2.micro')

print instance[0].id

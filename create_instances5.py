#!/usr/bin/env python

import boto3,sys
ec2 = boto3.resource('ec2')

svrlist=[
{'svrname':'ct-lin1','ipaddr':'10.96.0.100','secip':'10.96.1.100','prisubnet':'subnet-7f309d1b','secsubnet':'subnet-ddef43b9'},
{'svrname':'ct-lin2','ipaddr':'10.96.0.110','secip':'10.96.1.110','prisubnet':'subnet-7f309d1b','secsubnet':'subnet-ddef43b9'},
{'svrname':'ct-lin3','ipaddr':'10.96.0.120','secip':'10.96.1.120','subnet':'subnet-7f309d1b'},
{'svrname':'ct-lin4','ipaddr':'10.96.0.130','secip':'10.96.1.130','subnet':'subnet-7f309d1b'}
]

instance = ec2.create_instances(
    ImageId='ami-4fffc834',
    MinCount=1,
    MaxCount=1, 
    #SubnetId='subnet-f9eb08b2',
    #NetworkInterfaces=[{'AssociatePublicIpAddress':True,'DeviceIndex':0,'PrivateIpAddress':'10.32.0.181'}],
    NetworkInterfaces=[{'AssociatePublicIpAddress':True,'DeviceIndex':0,'PrivateIpAddress':svrlist[1]['ipaddr'],    'SubnetId':svrlist[1]['prisubnet']},
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Servername','Value': svrlist[1]['svrname']}]}],
    InstanceType='t2.micro')

print instance[0].id

#!/bin/env python
import boto3


ec2=boto3.resource('ec2')
network_interface = ec2.create_network_interface(
    Description='ctlin1',
    DryRun=False,
    Groups=[
        'sg-cf25ccbc',
    ],
    PrivateIpAddress='10.32.0.145', 
    SecondaryPrivateIpAddressCount=1,
    SubnetId='subnet-f9eb08b2',
)

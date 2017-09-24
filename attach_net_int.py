#!/bin/env python

import boto3

client=boto3.client('ec2')

#jresponse=network_interface.attach(
# DeviceIndex:wq

response=client.attach_network_interface(
DeviceIndex=1,
InstanceId='i-0b3a31e6f6448315b',
NetworkInterfaceId='eni-ad439713',
)
print response

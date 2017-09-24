#!/bin/env python

import boto3

client=boto3.client('ec2')
response=client.describe_network_interfaces()
print response


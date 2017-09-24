#!/bin/env python
import boto3,pprint

ec2=boto3.resource('ec2')
pp = pprint.PrettyPrinter(indent=4)

subnet = ec2.create_subnet(
    #AvailabilityZone='string',
    CidrBlock='10.96.1.0/24',
    VpcId='vpc-76cc2b0e',
)
pp.pprint(subnet)

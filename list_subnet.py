#!/bin/env python
import boto3,pprint 

ec2=boto3.resource('ec2')



pp = pprint.PrettyPrinter(indent=4)

#subnets = list(ec2.subnets.filter(Filters=filters))
subnets = list(ec2.subnets.all())
pp.pprint(subnets)

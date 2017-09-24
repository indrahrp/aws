#!/bin/env python
import boto3,pprint 

ec2=boto3.resource('ec2')



pp = pprint.PrettyPrinter(indent=4)

#subnets = list(ec2.subnets.filter(Filters=filters))
subnets = list(ec2.subnets.all())

for sub in subnets:
	pp.pprint("subnet {0}: zone: {1}  cidr: {2}  vpc_id : {3}".format(sub.subnet_id,sub.availability_zone,sub.cidr_block,sub.vpc_id))
	#pp.pprint(sub)

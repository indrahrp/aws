#!/bin/env python

import boto3

ec2=boto3.resource('ec2')
print str(ec2.instances.all())
for instance in ec2.instances.all():
	#server_name=instance.tags[0]['Value']
	server_name=instance.tags[0].get('Value')
	print "instance : " + str(instance.id) + " instance tag : " + str(server_name) + "pubIP "+ str(instance.public_ip_address)  + " privIP "+str(instance.private_ip_address) + " platform " + str(instance.platform) + " privdnsname "+ str(instance.private_dns_name) +" pubdnsname " + str(instance.public_dns_name) + " vpc " +str(instance.vpc_id) + " netinterf " + str(instance.network_interfaces) + " subnet " + str(instance.subnet_id) + " secgroup " + str(instance.security_groups) 
	#instance.terminate()
instance=ec2.Instance('i-045ab0cfa2f5be868')
#print str(instance.state)

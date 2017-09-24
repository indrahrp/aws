#!/bin/env python


import boto3

ec2=boto3.resource(service_name='ec2')


def create_and_configure_vpc():
	ec2=boto3.resource('ec2')
	vpc=ec2.create_vpc(CidrBlock='10.96.0.0/16')
        subnet=vpc.create_subnet(CidrBlock='10.96.0.0/24')
	internet_gateway = ec2.create_internet_gateway()
        response= internet_gateway.attach_to_vpc(VpcId=vpc.vpc_id)
	route_table = vpc.create_route_table()

        route_ig = route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway.internet_gateway_id)
	route_table.associate_with_subnet(SubnetId=subnet.id)
	return vpc


        sg = vpc.create_security_group(Group_name='Common', Description='Common Rules')	

	ip_ranges = [ {
	'CidrIp': '0.0.0.0/0'

	}]


	perms = [{  
	    'IpProtocol': 'TCP',
	    'FromPort': 80,
 	    'ToPort': 80,
	    'IpRanges': ip_ranges,
	}, {
	    'IpProtocol': 'TCP',
	    'FromPort': 443,
 	    'ToPort': 443,
	    'IpRanges': ip_ranges,
	}, {
	    'IpProtocol': 'TCP',
	    'FromPort': 22,
	    'ToPort': 22,
	    'IpRanges': ip_ranges,
	}]


	sg.authorize_ingress(IpPermissions=perms)

create_and_configure_vpc()



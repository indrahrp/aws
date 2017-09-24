#!/bin/env python

import boto3

ec2=boto3.resource('ec2')

vpc=ec2.Vpc('vpc-76cc2b0e')


sg = vpc.create_security_group(GroupName='Common', Description='Common Rules')

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





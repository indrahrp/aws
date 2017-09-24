#!/bin/env python

import boto3,pprint

pp = pprint.PrettyPrinter(indent=4)

client=boto3.client('ec2')

response = client.describe_route_tables(
Filters=[
  {
            'Name': 'vpc-id',
            'Values': [
                'vpc-76cc2b0e',
            ]
        },

],
)


print(response['RouteTables'][0]['Associations'][0]['RouteTableId'])

pp.pprint(response)


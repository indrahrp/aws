#!/bin/env python

import boto3

ec2=boto3.resource('ec2')
rt_tbl=ec2.route_tables.all()

for rt in rt_tbl:
	print "route tbl id " + rt.route_table_id + " vpc id " + rt.vpc_id + " routes " + str(rt.routes) + " routeattr " + str(rt.routes_attribute)

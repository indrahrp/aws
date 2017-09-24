#!/bin/env python
import boto.ec2.elb
regions = boto.ec2.elb.regions()
print "regions " + str(regions)
elb = regions[-1].connect()

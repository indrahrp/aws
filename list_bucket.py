#!/usr/bin/env python
import boto3
s3 = boto3.resource('s3')
clients3=boto3.client('s3')

#response = clients3.get_bucket_acl(
#    Bucket='string'
#
for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
    response = clients3.get_bucket_acl(
    Bucket=bucket.name)
    print "acl is " + str(response)	

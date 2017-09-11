#!/bin/env python
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

data=open('/etc/hosts','rb')
s3.Bucket('indrahrpdom').put_object(Key='hosts.test',Body=data)

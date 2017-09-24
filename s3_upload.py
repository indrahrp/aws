#!/bin/env python
import boto3
# Get the service client
s3 = boto3.client('s3')

# Upload tmp.txt to bucket-name at key-name
s3.upload_file("tmp.txt", "bucket-name", "indrahrpdom")

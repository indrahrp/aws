#!/bin/env python

import boto3

client = boto3.client('sqs')
response = client.list_queues(
    QueueNamePrefix='string'
)
print(" your queues : " + str(response))

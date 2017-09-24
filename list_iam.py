#!/bin/env python
import boto3

import boto3

# Create IAM client
iam = boto3.client('iam')

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

paginator = iam.get_paginator('list_roles')
for response in paginator.paginate():
    print(response)

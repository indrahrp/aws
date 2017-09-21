#!/bin/env python
import boto3  
from datetime import datetime, timedelta  
region = "us-east-1"  
ec2 = boto3.resource("ec2", region_name=region)  
def get_available_volumes():  
    available_volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    return available_volumes

print str(get_available_volumes())

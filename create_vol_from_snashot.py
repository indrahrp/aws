#!/bin/env python
import boto3,time

volumeid='vol-0ec47aeab82ddad70'
instanceid='i-0438130683c08f96b'
ec2 = boto3.resource('ec2')
snapshot = ec2.create_snapshot(VolumeId=volumeid, Description='description')
time.sleep(40)
volume = ec2.create_volume(SnapshotId=snapshot.id, AvailabilityZone='us-east-1b')
#volume = ec2.create_volume(SnapshotId=snapshot.id)
ec2.Instance(instanceid).attach_volume(VolumeId=volume.id, Device='/dev/sdy')
snapshot.delete()

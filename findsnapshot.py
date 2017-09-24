#!/bin/env python

import boto3


ec2=boto3.resource('ec2')

myaccountid='826606229734'
images = ec2.images.all()
images = [image.id for image in images]
for snapshot in ec2.snapshots.filter(OwnerIds=[myaccountid]):
#for snapshot in ec2.snapshots.all():
	print "snapshot owner id " + snapshot.owner_id + " state " + snapshot.state + " start time " + str(snapshot.start_time) + ' volid ' + snapshot.volume_id + ' snapshotid ' + snapshot.snapshot_id
   	snapshot.delete()
        	
   # r = re.match(r".*for (ami-.*) from.*", snapshot.description)
   # if r:
   #     print "snapshot name ami " + r.groups()[0]
   #     if r.groups()[0] not in images:
   #         print r.groups()[0]
   #         #snapshot.delete()

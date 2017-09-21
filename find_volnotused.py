#!/bin/env python
import boto3,re  
from datetime import datetime, timedelta  
region = "us-east-1"  
cloudwatch = boto3.client("cloudwatch", region_name=region)  
today = datetime.now() + timedelta(days=1) # today + 1 because we want all of today  
two_weeks = timedelta(days=14)  
start_date = today - two_weeks
myaccountid='826606229734'


ec2 = boto3.resource("ec2", region_name=region)  
def get_available_volumes():  
    available_volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    return available_volumes


def get_metrics(volume_id):  
    """Get volume idle time on an individual volume over `start_date`
       to today"""
    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EBS',
        MetricName='VolumeIdleTime',
        Dimensions=[{'Name': 'VolumeId', 'Value': volume_id}],
        Period=3600,  # every hour
        StartTime=start_date,
        EndTime=today,
        Statistics=['Minimum'],
        Unit='Seconds'
    )
    return metrics['Datapoints']

def is_candidate(volume_id):  
    """Make sure the volume has not been used in the past two weeks"""
    metrics = get_metrics(volume_id)
    if len(metrics):
        for metric in metrics:
            # idle time is 5 minute interval aggregate so we use
            # 299 seconds to test if we're lower than that
            if metric['Minimum'] < 299:
                return False
    # if the volume had no metrics lower than 299 it's probably not
    # actually being used for anything so we can include it as
    # a candidate for deletion
    return True

available_volumes = get_available_volumes()  
candidate_volumes = [  
    volume
    for volume in available_volumes
    if is_candidate(volume.volume_id)
]
# delete the unused volumes
# WARNING -- THIS DELETES DATA
cnt=0
for candidate in candidate_volumes:  
	print "candidate " + str(candidate)
        cnt=1

if cnt:
        yn=raw_input(" those candidate will be deleted Y/N")
	if yn == "Y":
		for candidate in candidate_volumes:  
			print "deleting candidate volume" + str(candidate)

        		candidate.delete()

#That's the an easy way to cleanup your volumes.

#Next you clean up your AMIs and then your snapshots:

instances = ec2.instances.all()  
my_images = ec2.images.filter(Owners=[myaccountid])  
# anything that's running or stopped we want to keep the AMI
good_images = set([instance.image_id for instance in ec2.instances.all()])  
# build a dictionary of all the images that aren't in good_images
my_images_dict = {image.id: image for image in my_images if image.id not in good_images}  
# now lets deregister all the AMIs older than two weeks

for image in my_images_dict.values():  
    created_date = datetime.strptime(
        image.creation_date, "%Y-%m-%dT%H:%M:%S.000Z")
    if created_date < start_date:
         image.deregister()


#The snapshots are also pretty easy to get rid of:


images = ec2.images.all()  
images = [image.id for image in images]  
for snapshot in ec2.snapshots.filter(OwnerIds=[myaccountid]):  
    r = re.match(r".*for (ami-.*) from.*", snapshot.description)
    if r:
	print "snapshot name ami " + r.groups()[0]
        if r.groups()[0] not in images:
            print r.groups()[0]
            #snapshot.delete()

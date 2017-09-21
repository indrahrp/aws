
import boto3,sys

# EC2 find instances
ec2 = boto3.resource('ec2')
base = ec2.instances.filter(InstanceIds=['id1', 'id2', 'id3'])

filters = [{
    'name': 'tenancy',
    'value': 'dedicated'
}]
filtered1 = base.filter(Filters=filters)

# Note, this does NOT modify the filters in ``filtered1``!
filters.append({'name': 'instance-type', 'value': 't1.micro'})
filtered2 = base.filter(Filters=filters)

print('All instances:')
for instance in base:
    print(instance.id)

print('Dedicated instances:')
for instance in filtered1:
    print(instance.id)

print('Dedicated micro instances:')
for instance in filtered2:
    print(instance.id)


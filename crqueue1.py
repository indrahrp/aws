#!/bin/env python
# Get the service resource
import boto3
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print('queue info after creation  : ' + queue.url)
print(queue.attributes.get('DelaySeconds'))


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))




#Get the service resource
sqs = boto3.resource('sqs')


# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')


response=queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})
# Create a new message
#response = queue.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))




response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'worldly'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

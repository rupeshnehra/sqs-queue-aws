# pip install boto3

import boto3

#set up sqs client call
sqs = boto3.resource('sqs', region_name=xxxxxx, aws_access_key_id=xxxxxxxxxxxxx,
        aws_secret_access_key=xxxxxxxxxxxxxxxxxxxx)

client = boto3.client('sqs')

response = sqs.create_queue(QueueName='test_queue.fifo', Attributes={'FifoQueue':'true', 
        'ContentBasedDeduplication': 'true'})

queue = sqs.get_queue_by_name(QueueName='test_queue.fifo')

# sending a message
create_message = queue.send_message(QueueUrl=QUEUE_URL, MessageBody='First queue started!', MessageGroupId='series1',
                 MessageDeduplicationId='Id1', MessageAttributes={})
print(create_message)

#consuming the message in queue
received_mesaages = []
messages = queue.receive_messages()
while len(messages)>0: 
    for message in messages:
        received_messages.append(message.body)
        print('Body: {0}'.format(message.body))
        message.delete()

response = queue.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=MESSAGE_ID)

response = queue.delete_messages(Entries=[{'Id': MESSAGE_ID,'ReceiptHandle': MESSAGE_BODY}])

response = client.delete_queue(QueueUrl=QUEUE_URL)





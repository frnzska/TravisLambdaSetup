import json
import logging
import os
import time
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_file(path):
    content = False
    cwd = os.getcwd()
    path = '/'.join([cwd, path])
    with open(path, 'r') as data:
        try:
            content = json.load(data)
        except Exception as e:
            logger.exception(e)
    return content

def some_function():
    return 'bailando'

def handler():
    spec = get_file('src/specs/event_specification.json')
    logger.info(json.dumps(spec))

# stuff to test aws mocking
kinesis = boto3.client('kinesis')
def some_kinesis_function():
    return kinesis.list_streams()

s3 = boto3.client('s3')
def s3_kinesis_function(bucket, s3_key, stream_name):
    data = s3.get_object(Bucket=bucket, Key=s3_key)['Body'].read().decode('utf-8')
    events = data.split('\n')
    if events[-1] == '':
        events = events[:-1]
    kinesis.put_record(StreamName=stream_name, Data= bytes(json.dumps(events[0]), 'utf-8'), PartitionKey='1')


def get_a_kinesis_date(stream_name):
    shard_id = 'shardId-000000000000'  # we only have one shard!
    shard_it = kinesis.get_shard_iterator(StreamName=stream_name, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")["ShardIterator"]
    while True:
        out = kinesis.get_records(ShardIterator=shard_it, Limit=2)
        if out['Records']:
            return out['Records'][0]['Data'].decode('utf-8')
        shard_it = out["NextShardIterator"]
        time.sleep(0.2)




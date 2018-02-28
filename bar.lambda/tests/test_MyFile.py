import boto3
from src.MyFile import some_function, s3_kinesis_function
import src
from localstack.utils.aws import aws_stack


def test_some_function():
    assert 'bailando' == some_function()
    assert 'helloWorld' != some_function()


def test_s3_kinesis_function():
    bucket = 'foo'
    s3_key = 'bar'
    stream = 'test'
    data = 'something'
    s3_resource = aws_stack.connect_to_resource('s3')
    s3_client = aws_stack.connect_to_service('s3')

    # create test bucket
    s3_resource.create_bucket(Bucket=bucket)

    s3_client.put_object(Bucket=bucket, Key=s3_key, Body=data)



    kinesis_client = aws_stack.connect_to_service('kinesis')
    kinesis = aws_stack.create_kinesis_stream(stream, delete=True)

    src.MyFile.s3 = s3_client
    src.MyFile.kinesis = kinesis_client

    src.MyFile.s3_kinesis_function(bucket, s3_key, stream)
    result = aws_stack.kinesis_get_latest_records(stream, 'shardId-000000000000', count=1)[0]['Data'].replace('"', '')
    assert result == data


import boto3
from src.MyFile import some_function
import src


def test_dummy():
    assert True

def test_some_function():
    assert 'bailando' == some_function()
    assert 'helloWorld' != some_function()


def test_kinesis_mock_dummy():
    stream_name = 'asdf'
    mock_kinesis_client = boto3.client('kinesis', endpoint_url='http://localhost:4567',
                                       aws_access_key_id='', aws_secret_access_key='')
    mock_kinesis_client.create_stream(StreamName=stream_name, ShardCount=1)
    src.MyFile.kinesis = mock_kinesis_client

    src.MyFile.some_kinesis_function()

    mock_kinesis_client.delete_stream(StreamName=stream_name)

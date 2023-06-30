import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1'
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=my_config)
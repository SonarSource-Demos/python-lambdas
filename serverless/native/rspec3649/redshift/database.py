import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1'
)

REDSHIFT_CLIENT = boto3.client('redshift-data', config=my_config)

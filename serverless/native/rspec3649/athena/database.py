import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1'
)

ATHENA_CLIENT = boto3.client('athena', config=my_config)
ATHENA_WORKGROUP = "my-athena-workgroup"
ATHENA_DB = "my-glue-database"
ATHENA_OUTPUT_LOCATION = "s3://athena-s3-serverlessapp/results/"

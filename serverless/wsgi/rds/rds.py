import os
import boto3
from flask import request


# /rds-data/safe1?i=CHARACTER_SETS
def safe1():
    client = boto3.client('rds-data')
    response = client.execute_statement(
        database=os.environ['DATABASE_NAME'],
        parameters=[
            {
                'name': 'table',
                'value': {
                    'stringValue': request.args.get('i')
                }
            }
        ],
        sql='select * from information_schema.tables where TABLE_NAME = :table',
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    return str(response)

# /rds-data/safe2?i=CHARACTER_SETS
def safe2():
    client = boto3.client('rds-data')

    response = client.execute_statement(
        sql='CREATE TABLE IF NOT EXISTS `test` (`test` VARCHAR(16))',
        database=os.environ['DATABASE_NAME'],
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    response = client.batch_execute_statement(
        parameterSets=[[
            {
                'name': 'table',
                'value': {
                    'stringValue': request.args.get('i')
                }
            }
        ]],
        sql='update test set test = :table where test = :table',
        database=os.environ['DATABASE_NAME'],
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    return str(response)

# /rds-data/vuln1?i=foo' or 1-- -
def vuln1():
    client = boto3.client('rds-data')
    response = client.execute_statement(
        sql='select * from information_schema.tables where TABLE_NAME = \'{}\''.format(request.args.get('i')),  # Noncompliant (S3649)
        database=os.environ['DATABASE_NAME'],
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    return str(response)

# /rds-data/vuln2?i=' OR BENCHMARK(50000000,ENCODE('MSG','some seconds delay'))-- -
def vuln2():
    client = boto3.client('rds-data')

    response = client.execute_statement(
        sql='CREATE TABLE IF NOT EXISTS `test` (`test` VARCHAR(16))',
        database=os.environ['DATABASE_NAME'],
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    response = client.batch_execute_statement(
        parameterSets=[[
            {
                'name': 'table',
                'value': {
                    'stringValue': request.args.get('i')
                }
            }
        ]],
        sql='update test set test = :table where test = \'{}\''.format(request.args.get('i')),  # Noncompliant (S3649)
        database=os.environ['DATABASE_NAME'],
        resourceArn=os.environ['DATABASE_ARN'],
        secretArn=os.environ['SECRET_ARN']
    )

    return str(response)


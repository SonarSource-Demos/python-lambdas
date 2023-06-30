import os
import boto3
from flask import request


# /simpledb/safe1?i=' or foo='bar
def safe1():
    client = boto3.client('sdb')
    domain = os.environ['DOMAIN_NAME']

    client.put_attributes(
        DomainName=domain,
        ItemName='foobar',
        Attributes=[
            {
                'Name': 'secret',
                'Value': '1234',
                'Replace': True
            },
            {
                'Name': 'foo',
                'Value': 'bar',
                'Replace': True
            },
        ]
    )

    secret = 0

    try:
        secret = int(request.args.get('i'))
    except ValueError as verr:
        pass

    response = client.select(
        SelectExpression="select * from `" + domain + "` where secret = '" + str(secret) + "'"
    )

    return str(response)


# /simpledb/vuln1?i=' or foo='bar
def vuln1():
    client = boto3.client('sdb')
    domain = os.environ['DOMAIN_NAME']

    client.put_attributes(
        DomainName=domain,
        ItemName='foobar',
        Attributes=[
            {
                'Name': 'secret',
                'Value': '1234',
                'Replace': True
            },
            {
                'Name': 'foo',
                'Value': 'bar',
                'Replace': True
            },
        ]
    )

    name = request.args.get('i')
    response = client.select(
        SelectExpression="select * from `" + domain + "` where secret = '" + name + "'"  # Noncompliant (S3649)
    )

    return str(response)

# /simpledb/vuln2?i=' or foo='bar
def vuln2():
    client = boto3.client('sdb')
    domain = os.environ['DOMAIN_NAME']

    client.put_attributes(
        DomainName=domain,
        ItemName='foobar',
        Attributes=[
            {
                'Name': 'secret',
                'Value': '1234',
                'Replace': True
            },
            {
                'Name': 'foo',
                'Value': 'bar',
                'Replace': True
            },
        ]
    )

    name = request.args.get('i')
    paginator = client.get_paginator('select')
    response_iterator = paginator.paginate(
        SelectExpression="select * from `" + domain + "` where secret = '" + name + "'"  # Noncompliant (S3649)
    )

    response = ''
    for i in response_iterator:
        response += str(i)

    return str(response)


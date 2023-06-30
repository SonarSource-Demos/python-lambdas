import os
import json

def lambda_handler(event, context):
    # in the query strings: foo=3*3
    result = eval(event["queryStringParameters"]["foo"]); # Noncompliant (S5334)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "result ": result
        })
    }
    
def parameterized_lambda_handler(event, context):
    # in the query strings: foo=3*3
    result = eval(event["queryStringParameters"]["foo"]); # Noncompliant (S5334)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "result ": result
        })
    }

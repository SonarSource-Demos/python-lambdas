import json
import os

# /test4/?foo=id
def test4(event, context):
    input = event['queryStringParameters']['foo']

    stream = os.popen(input)  # Noncompliant (S2076)
    output = stream.read()

    body = {
        "input": input,
        "output": output
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
from dynamo.compliant import getItem as getItemCompliant
from dynamo.compliant import scanAttributeValueList as scanAttributeValueListCompliant
from dynamo.compliant import scanExpressionAttributeValues as scanExpressionAttributeValuesCompliant
from dynamo.noncompliant import scanFilterExpression as scanFilterExpressionNoncompliant
from dynamo.noncompliant import queryFilterExpression as queryFilterExpressionNoncompliant

def mylambda(event, context):
    if event["queryStringParameters"]["dbid"] is None:
      return {
        "statusCode": 200,
        "body": json.dumps({
          "message": "invalid request, missing id param"
        })
      }

    sqlData = ""
    if event["queryStringParameters"]["dbid"] == "dynamo_compliant_getitem": 
        sqlData = getItemCompliant(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])
    
    elif event["queryStringParameters"]["dbid"] == "dynamo_compliant_scanattributevaluelist": 
        sqlData = scanAttributeValueListCompliant(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])

    elif event["queryStringParameters"]["dbid"] == "dynamo_compliant_scanexpressionfilter": 
        sqlData = scanExpressionAttributeValuesCompliant(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])

    elif event["queryStringParameters"]["dbid"] == "dynamo_noncompliant_scanfilterexpression": 
        sqlData = scanFilterExpressionNoncompliant(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])

    elif event["queryStringParameters"]["dbid"] == "dynamo_noncompliant_queryfilterexpression": 
        sqlData = queryFilterExpressionNoncompliant(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])

    return {
      "statusCode": 200,
      "body": json.dumps({
        "message": sqlData
      })
    }

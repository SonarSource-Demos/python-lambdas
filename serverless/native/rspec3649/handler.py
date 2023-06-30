import json
from athena.compliant import startQueryExecution as startQueryExecutionCompliant
from athena.noncompliant import startQueryExecution as startQueryExecutionNonCompliant
from redshift.compliant import executeStatement as executeStatementCompliant
from redshift.noncompliant import executeStatement as executeStatementNonCompliant

def mylambda(event, context):
    if event["queryStringParameters"]["dbid"] is None:
      return {
        "statusCode": 200,
        "body": json.dumps({
          "message": "invalid request, missing id param"
        })
      }

    sqlData = ""
    if event["queryStringParameters"]["dbid"] == "athena_compliant": 
        sqlData = startQueryExecutionCompliant(event["queryStringParameters"]["username"])
    
    elif event["queryStringParameters"]["dbid"] == "athena_noncompliant": 
        sqlData = startQueryExecutionNonCompliant(event["queryStringParameters"]["username"])

    elif event["queryStringParameters"]["dbid"] == "redshift_compliant": 
        sqlData = executeStatementCompliant(event["queryStringParameters"]["username"])
    
    elif event["queryStringParameters"]["dbid"] == "redshift_noncompliant": 
        sqlData = executeStatementNonCompliant(event["queryStringParameters"]["username"])

    return {
      "statusCode": 200,
      "body": json.dumps({
        "message": sqlData
      })
    }

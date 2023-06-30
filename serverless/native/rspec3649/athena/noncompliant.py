import athena.database
import time

def getQueryResults(queryid):
    response = athena.database.ATHENA_CLIENT.get_query_results(
        QueryExecutionId=queryid
    )

    return response
    
# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s3649/?dbid=athena_noncompliant&username=admin
# sqli try: https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s3649/?dbid=athena_noncompliant&username=admin'or'1'='1
def startQueryExecution(username):
    response = athena.database.ATHENA_CLIENT.start_query_execution(
        QueryString="SELECT * FROM users WHERE username = '"+username+"';", # taint is propagated
        QueryExecutionContext={
            'Database': athena.database.ATHENA_DB
        },
        ResultConfiguration={
            'OutputLocation': athena.database.ATHENA_OUTPUT_LOCATION
        },
        WorkGroup=athena.database.ATHENA_WORKGROUP
    ) # Noncompliant (s3649)

    time.sleep(5)

    return getQueryResults(response["QueryExecutionId"])

import redshift.database
import time

# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s3649/?dbid=redshift_compliant&username=admin
# sqli try: https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s3649/?dbid=redshift_compliant&username=admin' OR '1' = '1

def executeStatement(username):

    response = redshift.database.REDSHIFT_CLIENT.execute_statement(
        ClusterIdentifier="myredshiftclusterid",
        Database='dev',
        DbUser='redshift_data_api_user',
        Sql="select * from users where name = :username",
        Parameters=[
            {
                'name': 'username',
                'value': username
            }
        ],
        WithEvent=True
    ) # Compliant (s3649)

    time.sleep(5)

    response = redshift.database.REDSHIFT_CLIENT.get_statement_result(
        Id=response["Id"]
    )

    return response

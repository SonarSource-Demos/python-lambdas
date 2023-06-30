import dynamo.database

# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s5147/?dbid=dynamo_noncompliant_scanfilterexpression&username=admin&password=foo
# sqli try: https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s5147/?dbid=dynamo_noncompliant_scanfilterexpression&username=username > :p OR username&password=foo

# payload
# username > :p OR username

def scanFilterExpression(username, password):
    response = dynamo.database.DYNAMO_CLIENT.scan(
        FilterExpression= username + " = :u AND password = :p", 
        ExpressionAttributeValues={
            ":u": { 'S': "admin" },
            ":p": { 'S': password }
        },
        ProjectionExpression="username, password",
        TableName="users"
    ) # Noncompliant (s5147)

    return response


# don't know exactly how to exploit that because OR operator is not supported with query and KeyConditionExpression
# but it's definitely not a good practice to have a tainted KeyConditionExpression 

def queryFilterExpression(username, password):
    response = dynamo.database.DYNAMO_CLIENT.query(
        KeyConditionExpression= username + " = :u AND password = :p", 
        ExpressionAttributeValues={
            ":u": { 'S': "admin" },
            ":p": { 'S': password }
        },
        TableName="users"
    ) # Noncompliant (s5147)

    return response


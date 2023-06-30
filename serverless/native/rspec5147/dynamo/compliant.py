import dynamo.database

# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s5147/?dbid=dynamo_compliant_getitem&username=admin&password=foo

def getItem(username, password):
    response = dynamo.database.DYNAMO_CLIENT.get_item(
        TableName='users',
        Key={
            'username': {
                'S': username, # we expect a string here, nothing can happen
            },
            'password': {
                'S': password, # we expect a string here, nothing can happen
            }
        }
    )  #  Compliant (s5147)

    return response


# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s5147/?dbid=dynamo_compliant_scanattributevaluelist&username=admin&password=foo

def scanAttributeValueList(username, password):
    response = dynamo.database.DYNAMO_CLIENT.scan(
        ScanFilter={
            'username': {
                'AttributeValueList': [
                    {
                        'S': username # we expect a string here, nothing can happen
                    },
                ],
                'ComparisonOperator': 'EQ'
            }
        },
        TableName='users'
    ) # Compliant (s5147)

    return response


# https://API_ID.execute-api.us-east-1.amazonaws.com/dev/s5147/?dbid=dynamo_compliant_scanexpressionfilter&username=admin&password=foo

def scanExpressionAttributeValues(username, password):
    response = dynamo.database.DYNAMO_CLIENT.scan(
        FilterExpression= "username = :u AND password = :p", 
        ExpressionAttributeValues={
            ":u": { 'S': username }, # we expect a string here, nothing can happen
            ":p": { 'S': password } # we expect a string here, nothing can happen
        },
        ProjectionExpression="username, password",
        TableName="users"
    ) # Compliant (s5147)

    return response

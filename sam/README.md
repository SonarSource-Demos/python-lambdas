# AWS SAM app

AWS SAM application to illustrate Lambda entry points.


## Deploy

[Install and configure AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

```sh
sam build
sam deploy --guided
```

## Access API

Use the URL printed in the console once the deployment is done.

Go get the API key:
https://eu-west-1.console.aws.amazon.com/apigateway/home?region=eu-west-1#/api-keys

```sh
curl -H "x-api-key: <API_KEY>" -H "User-Agent: console.log(1+1)" https://qk0rrvq38g.execute-api.eu-west-1.amazonaws.com/Prod/function1
```

## Clean-up

```sh
aws cloudformation delete-stack --stack-name sam-app --region eu-west-1
```
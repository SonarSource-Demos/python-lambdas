# Athena
## Permissions
To create Athena DB resources, the following policies should be attached to the account:  
https://docs.aws.amazon.com/athena/latest/ug/managed-policies.html

## Add data in the users table
In the AWS Athena console, add some sql records to the `users` table:

```
INSERT INTO users (username, password) VALUES ('admin', 'foo'),('guest','bar')
```

## Prepare statements

https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements.html

In the AWS Athena console, create this prepare statement:

```
PREPARE select_users FROM
SELECT * FROM users WHERE username = ?
```

Prepare statements can be created with the aws-sdk API (and thus prone to SQL injection) but still uncommon, in Athena db, a prepare statement is more close to a view/named query than a prepare statement in traditional databases.

# Redshift

In the redshift aws console: 

## Create a table
```
CREATE TABLE users(name VARCHAR(40),password VARCHAR(40));
```

## Insert some data
```
insert into dev.public.users (name, password) values('admin', 'foo');
insert into dev.public.users (name, password) values('guest', 'bar');
```


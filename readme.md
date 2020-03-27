#### How to run DynamoDB locally and write data to a database using Python 

#### This small sample project was adapted from the DynamoDB Python tutorial here: 
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html

---

### Setup

#### Activate a virtualenv (python 3) and install packages from requirements
- This small project only requires boto3

#### Install AWS CLI
- Do you have AWS CLI installed?
- Type `aws` in the command line. If you see `command not found`, you don't have it.
- Get it here: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
- Then run `aws configure` and provide your AWS Access Key, AWS Secret Access Key, and region
- If you don't know where this info is stored, you'll have to retrieve/generate it from IAM in the AWS console: https://console.aws.amazon.com/iam

#### Download the the local/downloadable version of Dynamodb:
- https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip
- extract it to the root of this repo
- cd into `dynamodb_local_latest` and run this command in a terminal window:
- `java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`
- (from https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)
- leave this terminal window open and run other commands in a different terminal window/tab


#### List active tables in the running instance:
- for a quick check to make sure everything's running you can run this command:
- `aws dynamodb list-tables --endpoint-url http://localhost:8000`
- you will likely just see an empty object named 'TableNames' which is fine. now we can create a table

---


## TABLE OPERATIONS
#### The functions in table_operations.py pertain to an entire table 
#### In main.py uncomment each of the functions one at a time to independently execute them

## Create table
- first we create the Movies table by running `table_operations.create_table`
- it simply creates an empty table called 'Movies' using `year` and `title` as schema
- `KeySchema`, `AttributeDefinitions`, and `ProvisionedThroughout` are necessary to create a table.
- For information on these terms, please see:
- https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KeySchemaElement.html
- https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeDefinition.html 
- https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughput.html

## Describe table
- we can run describe_table.py to verify that it's been created.
- if we've already added data, then this command will have information about the items in the table as well

## Write to table
- here's where we load all the data from the moviedata.json file. this file specifies year, title, and info for each movie and writes an item into the database
- let's make sure the moviedata.json is in the root directory because we'll be loading its data into the local dynamodb
- this may take anywhere from 10 seconds to a few minutes depending on your computer

## Query or scan table
- now that the table contains data we can run queries against it
- as an example this function prompts for a year, then movies from that year will be returned

## Delete table
- yep this deletes the whole table
- this can't be undone

-----------

## CRUD OPERATIONS

#### The functions in crud_operations.py affect individual items within the table 

#### Create an item
- creates a new item in the table. this operation asks for the title of a new movie and its year of release
- other values in the info object are hardcoded (plot, rating) or omitted (actor, director, etc) for simple illustration purposes

#### Read an item
- enter the title and year
- this just returns the matched item

#### Update an item
- updates the specified fields. 'Little Black Book' is hardcoded for illustrative purposes.
- the rating, plot, and actors are updated
- this overwrites existing values and leaves alone the ones not mentioned (for example, if we just update the rating, the rating is changed, but actors, plot, year, etc remain untouched)

#### Delete an item
- deletes the item. specifically this deletes the item only if a condition is met (in this case, if the rating is below the hardcoded value
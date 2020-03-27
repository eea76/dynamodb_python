import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


def create_table(dynamodb, table_name):
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    )

    return f"{table_name} is {table.table_status}"


def query_or_scan(table):

    year = input('What year do you want to get movies from? ')

    print(f"Movies from {year}")

    response = table.query(
        KeyConditionExpression=Key('year').eq(int(year))
    )

    for i in response['Items']:
        print(i['year'], ":", i['title'])


def load_data(table):
    with open('moviedata.json') as json_file:
        movies = json.load(json_file, parse_float = decimal.Decimal)
        for movie in movies:
            year = int(movie['year'])
            title = movie['title']
            info = movie['info']

            print('Adding movie:', year, title)

            table.put_item(
                Item={
                    'year': year,
                    'title': title,
                    'info': info,
                }
            )


def describe_table(client, table):
    response = client.describe_table(TableName=table)
    print(response)


def delete(table, table_name):
    confirm_delete = input(f"Are you sure you want to delete the {table_name} table? y/n: ")
    if confirm_delete.lower() == 'y' or confirm_delete.lower() == 'yes':
        table.delete()
        print(f"{table_name} is deleted.")
    else:
        print('operation cancelled')

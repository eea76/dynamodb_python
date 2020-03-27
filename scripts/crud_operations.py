import decimal
import json
from botocore.exceptions import ClientError


def create_item(table, decimal_encoder):

    title = input("Enter the title of the new movie: ")
    year = int(input("What year did it come out? "))

    response = table.put_item(
        Item={
            'year': year,
            'title': title.title(),
            'info': {
                'plot': "Shit blows up in fiery flames and fans sob in happiness, desperate to pay more money to see the same thing again and again because their identities depend on their consumption of commercial entertainment.",
                'rating': decimal.Decimal(0)
            }
        }
    )

    print(f'success: {title.title()} has been created and added to {table}')
    print(json.dumps(response, indent=4, cls=decimal_encoder))


def read_item(table, decimal_encoder):

    title = input("Enter a movie title: ")
    year = int(input("Enter the year: "))

    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title.title()
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print('GetItem suceeded:')
        print(json.dumps(item, indent=4, cls=decimal_encoder))



def update_item(table, decimal_encoder):

    title = 'Little Black Book'
    year = 2004

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression='set info.rating = :r, info.plot=:p, info.actors=:a',
        ExpressionAttributeValues={
            ':r': decimal.Decimal(40.5),
            ':p': 'Way more shit blows up than we realized. It\'s actually incredible.',
            ':a': ['Gorvman Groverman']
        },
        ReturnValues="UPDATED_NEW"
    )

    print(json.dumps(response, indent=4, cls=decimal_encoder))
    print(f"{title} has been successfully updated.")


def delete_item(table, decimal_encoder):
    title = input("Enter a movie to delete: ")
    year = int(input("Enter the year: "))

    print('attempting a conditional delete')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title.title()
            },
            ConditionExpression='info.rating <= :val',
            ExpressionAttributeValues= {
                ":val": decimal.Decimal(5)
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print(json.dumps(response, indent=4, cls=decimal_encoder))
        print(f'{title} has been deleted from {table}.')


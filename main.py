import boto3

from decimal_helper import DecimalEncoder

from scripts import table_operations
from scripts import crud_operations

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table_name = "Movies"
table_object = dynamodb.Table(table_name)

# table operations
# print(table_operations.create_table(dynamodb, table_name))
# table_operations.load_data(table_object)
# table_operations.describe_table(client, table_name)
# table_operations.query_or_scan(table_object)
table_operations.delete(table_object, table_name)

# crud operations
# crud_operations.create_item(table_object, DecimalEncoder)
# crud_operations.read_item(table_object, DecimalEncoder)
# crud_operations.update_item(table_object, DecimalEncoder)
# crud_operations.delete_item(table_object, DecimalEncoder)


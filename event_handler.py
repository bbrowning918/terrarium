import os
import boto3

from dotenv import load_dotenv


class EventHandler:
    _table = None

    def __init__(self):
        load_dotenv()
        dynamodb = boto3.resource(
            service_name='dynamodb',
            region_name=os.environ.get('AWS_REGION_NAME'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        )
        self.table = dynamodb.Table(os.environ.get('AWS_DYNAMO_TABLE_NAME'))

    def submit(self, type, timestamp, payload={}):
        self.table.put_item(
            Item={
                'type': type,
                'timestamp':  timestamp,
                **payload
            }
        )

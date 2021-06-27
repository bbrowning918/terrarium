import os
import boto3

from botocore.exceptions import ClientError

from decimal import Decimal

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

    def submit(self, key, timestamp, payload=None):
        if payload is None:
            payload = dict()

        # cast floats
        for k, v in payload.items():
            if isinstance(v, float):
                payload[k] = Decimal(F'{v}')

        try:
            self.table.put_item(
                Item={
                    'key': key,
                    'timestamp': int(timestamp),
                    **payload
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])

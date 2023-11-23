import boto3
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    login = body['login']
    password = body['password']

    if login == 'admin' and password == 'XuB1God2dDBH':
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Correct data'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': "login or password isn't correct"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
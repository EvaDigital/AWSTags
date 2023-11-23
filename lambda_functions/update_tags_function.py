import json
import boto3


def lambda_handler(event, context):
    try:        
        body = json.loads(event['body'])
        arn = body['arn']
        new_tags = body.get('new_tags', None)
        delete_tags = body.get('delete_tags', None)
        arn_parts = arn.split(":")
        region = arn_parts[3]
        
        if delete_tags:
            delete_tags_func(arn, delete_tags)
        
        if new_tags:
            update_tags(arn, new_tags, region)

        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Tags updated successfully'}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    return response

def update_tags(arn, new_tags, region):
    client = boto3.client('resourcegroupstaggingapi', region_name=region)
    response = client.tag_resources(
        ResourceARNList=[arn],
        Tags=new_tags
    )
    print(response)


def delete_tags_func(arn, tags_to_delete):
    client = boto3.client('resourcegroupstaggingapi')
    response = client.untag_resources(
        ResourceARNList=[arn],
        TagKeys=tags_to_delete
    )
    print(response)

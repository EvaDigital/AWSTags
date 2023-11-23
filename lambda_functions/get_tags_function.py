import json
import boto3


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        arn = body['arn']
        existing_tags = get_existing_tags(arn)

        response = {
            'statusCode': 200,
            'body': json.dumps({'tags': existing_tags}),
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


def get_existing_tags(arn):
    client = boto3.client('resourcegroupstaggingapi')
    response = client.get_resources(
        ResourceARNList=[
            arn,
        ],
    )

    print(response)

    if 'ResourceTagMappingList' in response:
        resource_tag_mapping_list = response['ResourceTagMappingList']
        print(resource_tag_mapping_list)
        if resource_tag_mapping_list:
            tags = resource_tag_mapping_list[0].get('Tags', [])
            return {tag['Key']: tag['Value'] for tag in tags}

    return {}  

import boto3
import json


def lambda_handler(event, context):
    path = event.get('path', '/')

    if path == '/getresourses/by-name':
        return getresourses_by_name(event)
    elif path == '/getresourses/by-tag':
        return getresourses_by_tag(event)
    elif path == '/getresourses/by-resource':
        return getresourses_by_resours(event)
    elif path == '/getresourses/by-region':
        return getresourses_by_region(event)
    elif path == '/getresourses/by-owner':
        return pass_func()
    elif path == '/getresourses/get-tags-keys':
        return get_tags_keys()
    elif path == '/getresourses/get-resourses-names':
        return get_resourses_names()
    else:
        return getresourses(event)


def getresourses(event):
    client = boto3.client('resourcegroupstaggingapi')

    try:
        response = client.get_resources()

        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])
        
        arn_list = [{'arn': resource['ResourceARN'], 'tags': resource['Tags']} for resource in resources]

        return {
            'statusCode': 200,
            'body': json.dumps({
                'resources': arn_list
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

def pass_func():
    return {
            'statusCode': 200,
            'body': json.dumps({
                "message": "work"
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }


def getresourses_by_tag(event):
    try:
        client = boto3.client('resourcegroupstaggingapi')
        body = json.loads(event['body'])
        tag_key = body['tag_key']

        response = client.get_resources(
            TagFilters=[
                {
                    'Key': tag_key,
                    'Values': []
                }
            ]
        )
        arn_list = [{'arn': resource['ResourceARN'], 'tags': resource['Tags']} for resource in response.get('ResourceTagMappingList', [])]

        return {
            'statusCode': 200,
            'body': json.dumps({'resources': arn_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }


def getresourses_by_name(event):
    try:
        client = boto3.client('resourcegroupstaggingapi')
        body = json.loads(event['body'])
        response_name = body['response_name']

        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])
        
        filtered_resources = [resource for resource in resources if 'ResourceARN' in resource and response_name in resource['ResourceARN'].split(':')[-1]]

        arn_list = [{'arn': resource['ResourceARN'], 'tags': resource['Tags']} for resource in filtered_resources]

        return {
            'statusCode': 200,
            'body': json.dumps({'resources': arn_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

def getresourses_by_resours(event):
    try:
        client = boto3.client('resourcegroupstaggingapi')
        body = json.loads(event['body'])
        resours_name = body['resours_name']

        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])
        
        filtered_resources = [resource for resource in resources if 'ResourceARN' in resource and resours_name in resource['ResourceARN'].split(':')[2]]

        arn_list = [{'arn': resource['ResourceARN'], 'tags': resource['Tags']} for resource in filtered_resources]

        return {
            'statusCode': 200,
            'body': json.dumps({'resources': arn_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }


def getresourses_by_region(event):
    try:
        body = json.loads(event['body'])
        region = body['region']

        client = boto3.client('resourcegroupstaggingapi', region_name=region)
        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])
        arn_list = [{'arn': resource['ResourceARN'], 'tags': resource['Tags']} for resource in resources]

        return {
            'statusCode': 200,
            'body': json.dumps({'resources': arn_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    

def get_tags_keys():
    try:
        client = boto3.client('resourcegroupstaggingapi')
        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])

        unique_tag_keys = set()

        for resource in resources:
            tags = resource.get('Tags', [])
            for tag in tags:
                tag_key = tag.get('Key')
                unique_tag_keys.add(tag_key)

        unique_tag_keys_list = list(unique_tag_keys)

        return {
            'statusCode': 200,
            'body': json.dumps({'keys': unique_tag_keys_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    

def get_resourses_names():
    try:
        client = boto3.client('resourcegroupstaggingapi')
        response = client.get_resources()

        resources = response.get('ResourceTagMappingList', [])

        unique_resource_names = set()

        for resource in resources:
            resource_arn = resource.get('ResourceARN')

            if resource_arn:
                resource_name = resource_arn.split(':')[2]
                unique_resource_names.add(resource_name)

        resource_names_list = list(unique_resource_names)

        return {
            'statusCode': 200,
            'body': json.dumps({'resource_names': resource_names_list}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
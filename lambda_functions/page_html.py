import json

def lambda_handler(event, context):
    path = event.get('path', '/')

    if path == '/index/login':
        with open("./login.html", "r") as file:
            html_content = file.read()
    elif path == '/index/home':
        with open("./home.html", "r") as file:
            html_content = file.read()
    elif path == '/index/tags':
        with open("./index.html", "r") as file:
            html_content = file.read()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }

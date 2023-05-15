import json


def lambda_handler(event, context):
    """
    This is probably the simplest Lambda function you can build. The Lambda execution environment
    will run the code of this function on demand
    """
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

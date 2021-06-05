import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion":"1111111111111","temp":event})
    }

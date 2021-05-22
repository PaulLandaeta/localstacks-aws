import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion":"23456789fghjk","temp":"temp"})
    }

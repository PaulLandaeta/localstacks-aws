import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context): 
    """AWS Lambda Function entrypoint to create bill

    Parameters
    ----------
    event: dict, required
        facturaId:

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    -------
    boolean

    """
    body = json.loads(event['body'])
    queue_name = 'DemoStandardQueue'

    try:
        
        return {
            'statusCode': 200,
            'body': json.dumps({"message": 'Factura Recibida a la cola', "event": body})
        }
    
    except ClientError as err:
        return {
            'statusCode': 401,
            'error_message': err.response['Error']['Message']
        }


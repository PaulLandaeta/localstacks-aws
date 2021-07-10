import json
import boto3
from botocore.exceptions import ClientError

def send_factura(queue_name,msg_body):
    """

    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """

    # Send the SQS message
    sqs_client = boto3.client('sqs')    
    sqs_queue_url = sqs_client.get_queue_url( QueueName=queue_name)['QueueUrl'] 
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=json.dumps(msg_body)) 
    except ClientError as e:
        return None
    return msg


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
    factura_id = body.get("facturaId")
    queue_name = 'DemoStandardQueue'

    
    
    if not factura_id:
        raise ValueError("Factura Invalida")
    try:
        
        msg = send_factura(queue_name,event)
        return {
            'statusCode': 200,
            'body': json.dumps({"message": 'Factura enviada a la cola', "event": body, 'msg': msg})
        }
    
    except ClientError as err:
        return {
            'statusCode': 401,
            'error_message': err.response['Error']['Message']
        }
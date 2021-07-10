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
    sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/556356385512/DemoStandardQueue'
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=json.dumps(msg_body)) 
    except ClientError as e:
        return e.response['Error']['Message']
    return msg


def validar_informacion(event):
    body = json.loads(event['body'])
    ci_nit = body['ci_nit']
    razon_social = body['razon_social']
    idSucursal = body['idSucursal']
    efectivo = body['efectivo']
    if not ci_nit:
        return ("Factura Invalida")
    if not razon_social:
        return ("Factura Invalida")
    if not idSucursal:
        return ("Factura Invalida")
    if not efectivo:
        return ("Factura Invalida")

    return ("Facturar")

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

    valida = validar_informacion(event)
    if valida != 'Facturar':
         return {
            'statusCode': 401,
            'body': valida
        }

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


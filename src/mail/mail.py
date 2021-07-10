import json
import boto3
import smtplib, ssl
from botocore.exceptions import ClientError


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "paulwilkerlf3@gmail.com"  # Enter your address
receiver_email = "naujjuan91@gmail.com"  # Enter receiver address
password = "colegio123loco123"
message = """\
Subject: Hi there

This message is sent from Python."""


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
    # body = json.loads(event['body'])
    print(event)
    queue_name = 'DemoStandardQueue'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    try:
        
        return {
            'statusCode': 200,
            'body': json.dumps({"message": 'Factura Recibida a la cola'})
        }
    
    except ClientError as err:
        return {
            'statusCode': 401,
            'error_message': err.response['Error']['Message']
        }


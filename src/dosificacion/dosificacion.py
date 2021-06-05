import json
import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.client('dynamodb')
GET = 'GET'


def lambda_handler(event, context):
    httpMethod = event['httpMethod']
    try:
        if httpMethod == GET:
            return get_dosificacion(event)
        else:
            return insert_dosificacion(event)
    except ClientError as e:
        return {
            'statusCode': 401,
            'error_message': e.response['Error']['Message']
        }


def get_dosificacion(event):
    # TODO get the dosificacion a partir del key (dosif_nro_autorizacion+)
    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion": "1111111111111", "event": event})
    }


def insert_dosificacion(event):
    body = json.loads(event['body'])
    dosif_nit = body['dosif_nit']

    dosif_nro_autorizacion = body['dosif_nro_autorizacion']
    control = dosif_nit+dosif_nro_autorizacion
    try:

        dynamodb.put_item(TableName='Dosificacion', Item={'Id_dosificacion': {
                          'S': control}, 'event': {'S': event['body']}})

        return {
            'statusCode': 200,
            'body': json.dumps({"dosificacion": control, "event": body})
        }
    except ClientError as e:
        return {
            'statusCode': 401,
            'error_message': e.response['Error']['Message']
        }

import json
import boto3

dynamodb = boto3.client('dynamodb')
GET = 'GET'

def lambda_handler(event, context):
    httpMethod = event['httpMethod'] 

    if httpMethod == GET:
        return get_dosificacion(event)
    else:
        return insert_dosificacion(event)
    
def get_dosificacion(event):
    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion":"1111111111111", "event": event})
    }

def insert_dosificacion(event):
    body = json.loads(event['body'])
    dosif_nit = body['dosif_nit']

    dosif_nro_autorizacion = body['dosif_nro_autorizacion']
    control = dosif_nit+dosif_nro_autorizacion
    dynamodb.put_item(TableName='Dosificacion', Item={'Id_dosificacion':{'S':control}})

    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion":"1111111111111","temp":control})
    }

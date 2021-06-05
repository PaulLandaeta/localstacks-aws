import json
import boto3
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])


    dosif_nit = body['dosif_nit']
    dosif_nro_autorizacion = body['dosif_nro_autorizacion']
    control = dosif_nit+dosif_nro_autorizacion
    dynamodb.put_item(TableName='Dosificacion', Item={'Id_dosificacion':{'S':control},'key2':{'S':event['body']}})

    return {
        'statusCode': 200,
        'body': json.dumps({"dosificacion":"1111111111111","temp":control})
    }



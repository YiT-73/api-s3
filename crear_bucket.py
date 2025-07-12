import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])  # decodificar el JSON del body
    nombre_bucket = body['bucket']

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': f'Bucket {nombre_bucket} creado exitosamente.'
        })
    }

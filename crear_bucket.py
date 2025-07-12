import boto3
import json

def lambda_handler(event, context):
    try:
        # Parsear correctamente el JSON desde el body
        body = json.loads(event['body'])  # <--- esto es crítico
        nombre_bucket = body['bucket']

        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=nombre_bucket)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': f'Bucket {nombre_bucket} creado exitosamente.'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

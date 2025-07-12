import boto3
import base64

def lambda_handler(event, context):
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    archivo = event['body']['nombre_archivo']
    contenido = base64.b64decode(event['body']['contenido_base64'])

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=f'{directorio}/{archivo}', Body=contenido)

    return {
        'statusCode': 200,
        'mensaje': f'Archivo {archivo} subido a {bucket}/{directorio}.'
    }
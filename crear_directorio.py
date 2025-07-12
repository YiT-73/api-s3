import boto3

def lambda_handler(event, context):
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=(directorio+'/'))
    
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {directorio}/ creado en el bucket {bucket}.'
    }
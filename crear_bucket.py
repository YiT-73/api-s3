import boto3
import json
import os

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket']
        region = os.environ.get('AWS_REGION', 'us-east-1')

        s3 = boto3.client('s3', region_name=region)

        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )

        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': f'Bucket {bucket_name} creado exitosamente en {region}.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

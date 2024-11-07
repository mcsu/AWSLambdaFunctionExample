import boto3, json

def lambda_handler(event, context):
    
   
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

'''
Purpose:
    extract text from image to return data
'''
import json

import boto3

from utils import get_simpliflied_context, to_user_from_s3ol


s3_client = boto3.client('s3')
rekog_client = boto3.client('rekognition')


def lambda_handler(event, context):
    easy_context = get_simpliflied_context(event)
    
    image = s3_client.get_object(
            Bucket=easy_context["bucket"],
            Key=easy_context["key"]
        )

    image = image.get("Body").read()
        
    response = rekog_client.detect_text(Image={
        'Bytes': image
    })
    response =  [ line['DetectedText'] for line in response['TextDetections'] ]
    response = " ".join(response)
    
        
    to_user_from_s3ol(
            data=response,
            token=easy_context["token"],
            route=easy_context["route"]
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success operation!')
    }



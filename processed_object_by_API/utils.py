'''
Purpose:
    define a utils methods to process data.
'''
import boto3


S3Client = boto3.client('s3')


def get_simpliflied_context(context):
    '''
    Purpose:
        simplified a context of s3 object lambda.
    Params:
        - context (dict) : context of s3 object lambda.
    return dict with data of context
    '''
    simple_context = dict()
    simple_context["object_url"] = context["getObjectContext"]["inputS3Url"]
    simple_context["route"] = context["getObjectContext"]["outputRoute"]
    simple_context["token"] = context["getObjectContext"]["outputToken"]
    simple_context["bucket"] = context["configuration"]["payload"]
    simple_context["key"] = context["userRequest"]["url"].split("/")[-1]
    return simple_context


def to_user_from_s3ol(data, token, route):
    '''
    Purpose:
        return data to S3 object lambda.
    Params:
        - data (bytes): data will come back to user.
        - token (string): token to autenticate.
        - route (string): route to send data.
    return None
    '''
    S3Client.write_get_object_response(
            Body=data,
            RequestRoute=route,
            RequestToken=token,
        )



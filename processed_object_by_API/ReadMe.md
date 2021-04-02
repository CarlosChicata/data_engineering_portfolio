# Processed Object By API
## Purpose
Create an API to get richest data from image-type raw data stored in S3. The answer can be in json format.

## Context
We are service providers and it leads us to store images with text from our clients in addition to some information about it that is in a database.

We have reached an agreement with a client on the use of this information that we have richer. To comply, we will create an API service that extracts the text from the image and indicates the detailed information of the image and its creation. 

## Tools and developer enviroment
We use AWS cloud to create this service. I will use followed service.
* Rekognition.
* S3.
* API Gateway.
* Lambda function.

The programming languaje to use to implement is python 3.8. Boto3 1.17.39 is a AWS SDK to connect with AWS Service.

## Diagrams

Soon on

## What services does money represent?

Soon on

## Limits

Soon on

## Learned lesson
Those are:

1) The rekognition services to detect text in image is available in specified regions. i need to move Canada region (ca-central-1) to north of virgin region (us-east-1) to use. I need to check what region has available services.

## Version
Current versión is 0.1.0

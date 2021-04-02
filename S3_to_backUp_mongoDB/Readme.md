# project: Automatic backUp in mongo using AWS
## Purpose
In EC2, create cronjob will use a script to create a backup of database in mongo and automatic store it in S3.

## Tech Tool
The service i will use are:
- AWS EC2
- MongoDB
- AWS CLI

I will use bash to program the processs to get a backup; and cronjob of linu OS to generate a cronjob.

## Context
Your linux server; EC2 in this example; has a mongodb instance to running. This mongo instance is standalone. <br>
you need to generate a backup of database every day at 5am and save it in bucket S3.

## Tasks
- [X] Create script to create a backup of database in mongo.
- [ ] Create S3 in Bucket.
- [ ] Send backup to S3 bucket.
- [ ] Create EC2 and store script.
- [ ] Create a cronjob in EC2 use the script and run 5am every day.

## Diagram

working ....

## What services does money represent?

working ....

## Learned lesson

1) know more about bash programming language.

## Version
Current is 0.0.1

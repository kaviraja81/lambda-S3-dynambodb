import json
import boto3
import datetime
from botocore.exceptions import ClientError

#get the resource
dynamodb=boto3.resource('dynamodb')
client=boto3.client('dynamodb')
s3=boto3.resource('s3')


def lambda_handler(event, context):
    # TODO implement
    #dynamodb table test is assigned to table resource
    table=dynamodb.Table('S3ObjectTable')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

   # SCANS tables to find the count of the number of items
   # the new_num is the partition hash key to be used

    response=table.scan(
        TableName='S3ObjectTable'
          )
    item = response['Items']
    # find the maximum number in the scan of the table
    listnum=[]
    for x in range(0,len(item)) :
        listnum.append(int(item[x]['num']))

    # Gets the new id for the dynamodb table
    new_num=max(listnum)+1

    #put_item is used to write a record in dynamodb Table
    table.put_item (
        Item={
            'DateAdded' : datetime.datetime.utcnow().isoformat(),
             'num'      : new_num,
             'Objectname'  : key
        })

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully added')
     }

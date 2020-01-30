# lambda-S3-dynambodb 
PRE-REQUISITES
   Create a new dynamodb table S3ObjectTable with the partition key as num with type Number. 
Create a lambda function with dynamodb.py file as the lambda code. Add the S3 bucket as the trigger to the lambda function. 
This lambda function writes the object /files added to the S3 bucket into the dynamodb table. It writes the number , timestamp as well as the file name that was added to the S3 bucket into the dynamodb table

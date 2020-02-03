# lambda-S3-dynambodb 
1.PRE-REQUISITES

   Create a new dynamodb table S3ObjectTable with the partition key as num with type Number. 

2.LAMBDA STEPS

Create a lambda function with dynamodb.py file as the lambda code. 

Add the S3 bucket as the trigger to the lambda function. 

3.LAMBDA FUNCTIONALITY

This lambda function writes the object /files added to the S3 bucket into the dynamodb table. It writes the number , timestamp as well as 
the file name that was added to the S3 bucket into the dynamodb table. The code is written in Python.


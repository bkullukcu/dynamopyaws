import boto3 
from boto3 import dynamodb 
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


dynamodb_session = Session(aws_access_key_id='access_key_id',
          aws_secret_access_key='secret_access_key',
          region_name='region')

dynamodb = dynamodb_session.resource('dynamodb')

table=dynamodb.Table('table_name')

def sendDataDb():
    try:
        response = table.get_item(Key={item_id': 'id','ts': epochtimeint})    
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        for res in response:
            return response['Item']['random_string']
            break
while True:
    try:
        sendDataDb()   
    except ClientError as e:
        print(e.response['Error']['Message'])
        break
    except:
        print('Not found')
        break
    else:       
        if sendDataDb() == response['Item']['random_string']:
            print('sth happened')
            break
        else:
            print('sth else happened')
            break

# This is a Lambda layer that handles access to the FireStore databases

import json
import os
import boto3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#we identify the region where the code is running
regionName= os.environ.get('AWS_REGION')
if (regionName == 'None'):
    regionName= "us-west-2"

#we get the certificate from S3
s3 = boto3.resource('s3',region_name=regionName)
BUCKET_NAME = 'hereiamkey'
KEY = 'hereiam-bfaa5-firebase-adminsdk-9ploa-106ba0d329.json'

#write certificate in a file
filename = '/tmp/certificate.json'
s3.Bucket(BUCKET_NAME).download_file(KEY, filename)

#load the certificate
cred = credentials.Certificate(filename)
#initialize the firebase client
firebase_admin.initialize_app(cred)
db = firestore.client()

#delete the certificate file
os.remove(filename)

#Retrieve all existing documents from a Firebase collection
def getDocuments(collection):
    scenarios = db.collection(collection)
    docs = scenarios.get()
    return docs

#Create a payment entry in Firebase
def createPayment(latitude,longitude,price,date_of_transaction,vendor,alert):
    payments_ref = db.collection('payments')

    inputs = {
        'latitude' : latitude,
        'longitude' : longitude,
        'price' : price,
        'date_of_transaction' : date_of_transaction,
        'vendor': vendor,
        'alert' : alert
    }

    payments_ref.document().set(inputs)



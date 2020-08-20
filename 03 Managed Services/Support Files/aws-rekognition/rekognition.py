#*********************************************************************************************************************
# Author - Nirmallya Mukherjee
# This program demonstrates various AWS Rekognition APIs
# This is provided as part of the training without any warrenty. Use the code at your own risk.

# Please SSH to the EC2 instance and do the following
# ssh -i PEM-FILE ubuntu@IP

# sudo apt install python3-pip -y
# sudo apt install zip -y
# sudo apt install awscli -y

# pip3 install boto3

# aws configure

# sudo chmod 777 -R /opt
# cd /opt
# wget https://storage.googleapis.com/skl-training/aws-codelabs/rekognition/aws-rekognition.zip
# unzip aws-rekognition.zip
#*********************************************************************************************************************


import boto3
import json


def rekognize(client, imageFile):
    #We will read the file from the local disk instead from S3
    with open(imageFile, 'rb') as image:
        filecontents = image.read()
        rekog_text = client.detect_text(Image={'Bytes': filecontents})
        rekog_labels = client.detect_labels(Image={'Bytes': filecontents})
        rekog_faces = client.detect_faces(Image={'Bytes': filecontents})
        #response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    return (rekog_text, rekog_labels, rekog_faces)


def extractText(rekog_response):
    print("==============================================================================================================================")
    #print(json.dumps(rekog_response, indent=4, sort_keys=True))
    textDetections=rekog_response['TextDetections']
    print('Detected text')
    for text in textDetections:
        print(text['DetectedText'], end=" ")
    print("\n")


def extractLabels(rekog_response):
    print ("=============================================================================================================================")
    #print(json.dumps(rekog_response, indent=4, sort_keys=True))
    print('Detected labels in ' + imageFile)
    for label in rekog_response['Labels']:
        print("Label name is", label['Name'], "with parents", label['Parents'], "having confidence", label['Confidence'])
    print("")


def extractFaces(rekog_response):
    print("=============================================================================================================================")
    #print(json.dumps(rekog_response, indent=4, sort_keys=True))
    print('Details of faces in ' + imageFile)
    for faceDetail in rekog_response['FaceDetails']:
        print("Face found with", faceDetail['Confidence'],"% confidence", "Features found are", end=" ")
        for feature in faceDetail['Landmarks']:
            print(feature['Type'], end=" ")
        print("")


if __name__ == "__main__":
    client=boto3.client('rekognition')
    #Captcha.jpg Observation.jpeg soup-spoon.jpeg DennisRitchieVSSteveJobs.jpeg cheap-vs-quality.jpeg Dilbert-officepolitics.jpeg
    #imageFile = 'DennisRitchieVSSteveJobs.jpeg'
    #imageFile = 'cheap-vs-quality.jpeg'
    #imageFile = 'Captcha.jpg'
    #imageFile = 'soup-spoon.jpeg'
    #imageFile = 'hinditext.jpg'
    #imageFile = 'textonmobile.jpg'
    #imageFile = 'Textinsidemirror.jpg'
    #imageFile = 'ambassadornptext.jpg'
    imageFile = 'multitext.jpg'
    rekog_text, rekog_labels, rekog_faces = rekognize(client, imageFile)
    extractText(rekog_text)
    extractLabels(rekog_labels)
    extractFaces(rekog_faces)
    print("\nAll done.")

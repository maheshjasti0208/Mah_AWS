#*********************************************************************************************************************
# Author - Nirmallya Mukherjee
# This program demonstrates various AWS Comprehend APIs
# This is provided as part of the training without any warrenty. Use the code at your own risk.
# https://docs.aws.amazon.com/comprehend/latest/dg/functionality.html
#*********************************************************************************************************************

import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
text = "The number of patients who were presenting with critical illness all at the same time was staggering, remembers Meyer, a professor of medicine at the Hospital of the University of Pennsylvania. But it wasn’t just that these patients were really sick—it was that they were sick in a startling variety of ways. Some had cardiac issues. Others had blood clots in their legs. Then there were those who developed pneumonia and related respiratory problems. Organ failure affected some. The list went on and on.La technologie peut vous donner du bonheur"

print("Calling DetectDominantLanguage")
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectSyntax')
print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('All done\n')


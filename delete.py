import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='946c5bc6913a2abad3d285c1312e6281b2ff94f2')

print(json.dumps(visual_recognition.delete_classifier(classifier_id='Leaves_vs_tomato_226557840'), indent=2))
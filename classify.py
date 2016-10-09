import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

#visual_recognition = VisualRecognitionV3('2016-05-20', api_key='946c5bc6913a2abad3d285c1312e6281b2ff94f2')
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='ee46d3221bdb98c4bcf24714689087305c7bd98b')

#file_to_test = 'test/1024.jpg'
file_to_test = 'test/reale4.jpg'

with open(join(dirname(__file__), file_to_test), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0,
                                                 classifier_ids='leave_vs_tomato'), indent=2))

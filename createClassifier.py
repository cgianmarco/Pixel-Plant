import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='946c5bc6913a2abad3d285c1312e6281b2ff94f2')

with open(join(dirname(__file__), 'archives/type1.zip'), 'rb') as type1, \
        open(join(dirname(__file__), 'archives/type2.zip'), 'rb') as type2:
    print(json.dumps(visual_recognition.create_classifier('Leaves', type1_positive_examples=type1, type2_positive_examples=type2), indent=2))

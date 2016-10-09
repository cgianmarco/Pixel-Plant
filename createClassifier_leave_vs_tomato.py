import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='946c5bc6913a2abad3d285c1312e6281b2ff94f2')

with open(join(dirname(__file__), 'archives/pomodori.zip'), 'rb') as pomodoro, \
        open(join(dirname(__file__), 'archives/foglie.zip'), 'rb') as foglia, \
        open(join(dirname(__file__), 'archives/negativi.zip'), 'rb') as negativi:
    print(json.dumps(visual_recognition.create_classifier('leave_vs_tomato', pomodoro_positive_examples=pomodoro, foglia_positive_examples=foglia, negative_examples=negativi), indent=2))

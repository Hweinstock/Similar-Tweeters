from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CompSerializer
from .models import ComparisonData
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render

from text_model.config_files.config import get_text_object
from text_model.analyzer.text_objects.text import analyze_config
from text_model.analyzer.comparison import Comparison
from text_model.analyzer.model.model import run_on_object
from text_model.data_cleaner.clean_twitter_data import clean_tweet
from twitter.main import tweets_from_handle, read_in_top_users

# Create your views here.


class CompView(viewsets.ModelViewSet):
    serializer_class = CompSerializer
    queryset = ComparisonData.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:

        Overwrite retrieve method for CompViewSet to wait for comp to be made. (Does comp on retrieve call.)
        """
        comp_id = kwargs['pk']
        comp_qset = ComparisonData.objects.filter(id=comp_id)
        if len(comp_qset) > 1:
            print("QuerySet returned multiple objects for single id!")

        comp = comp_qset[0]

        TextObject = get_text_object(comp.label)
        Text1 = TextObject(comp.text1, raw_text=True)
        Text2 = TextObject(comp.text2, raw_text=True)

        CompObject = Comparison(Text1, Text2)

        result, percent = run_on_object(CompObject)

        return Response({'result': result,
                         'percent': percent})


@api_view(['GET'])
def headers(request):
    configs = analyze_config()
    headers = configs['headers']

    return Response({'Headers': headers})


@api_view(['POST'])
def create_text_objects(request):
    texts = request.data['text']
    label = request.data['label']

    TextObject = get_text_object(label)
    Text1 = TextObject(texts['box1'], raw_text=True)
    Text2 = TextObject(texts['box2'], raw_text=True)

    return Response({'text_objects': [Text1.report(), Text2.report()]})


@api_view(['GET'])
def get_recent_tweets(request):
    twitter_handle = request.GET.get('username', None)
    tweets = tweets_from_handle(twitter_handle)

    Tweet = get_text_object('tweet')
    cleaned_tweets = [clean_tweet(tw) for tw in tweets]
    total_text = ' '.join(cleaned_tweets)

    total_text_obj = Tweet(total_text, raw_text=True)
    total_text_rep = total_text_obj.report()

    print(read_in_top_users())

    return Response({"tweet": total_text,
                     "report": total_text_rep,
                     })

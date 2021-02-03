from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CompSerializer, TextObjectSerializer
from .models import ComparisonData, TextObjectData
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from django.shortcuts import render


from text_model.config_files.config import get_text_object
from text_model.analyzer.text_objects.text import analyze_config
from text_model.analyzer.comparison import Comparison
from text_model.analyzer.model.model import run_on_object
from text_model.data_cleaner.clean_twitter_data import text_from_user

# Create your views here.


class TextObjectView(viewsets.ModelViewSet):
    serializer_class = TextObjectSerializer
    queryset = TextObjectData.objects.all()

    @action(detail=False, url_path="doesExist")
    def check_if_exists(self, request, pk=None):
        query_author = request.GET.get('author', None)
        query_set = TextObjectData.objects.filter(author=query_author)

        if len(query_set) == 0:
            return Response({'status': False})
        else:
            return Response({'status': True})
    #
    # @action(detail=False, url_path="fromUsername", methods=['post'])
    # def create_from_username(self, request, pk=None):
    #     username = request.data["username"]
    #     tweets = text_from_user(username)
    #     total_text = ' '.join(tweets)
    #
    #     data = {"label": "from_username",
    #             "author": username,
    #             "text": total_text,
    #             }
    #
    #     self.create(Request())
    #
    #     print(TextObjectData.objects.all())


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

        CompObject = Comparison(Text1.to_vector, Text2.to_vector)

        result, percent = run_on_object(CompObject)

        return Response({'result': result,
                         'percent': percent})


@api_view(['GET'])
def id_and_text_from_user(request):
    username = request.GET.get('username', None)
    tweets = text_from_user(username)
    total_text = ' '.join(tweets)

    data = {"label": "from_username",
            "author": username,
            "text": total_text,
            }

    return Response(data)


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
def compare_recent_tweets(request):
    # Extract the params from GET request.
    twitter_handle = request.GET.get('username', None)

    # Get recent tweets
    tweets = text_from_user(twitter_handle)

    # Create 'Tweet' objects
    TweetObj = get_text_object('tweet')

    # Combine all tweet text into one giant tweet.
    total_text = ' '.join(tweets)
    total_text_obj = TweetObj(total_text, raw_text=True)
    total_text_rep = total_text_obj.report()

    return Response({"tweet": total_text,
                     "report": total_text_rep,
                     })

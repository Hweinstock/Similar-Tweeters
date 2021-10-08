from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CompSerializer, TextObjectSerializer
from .models import ComparisonData, TextObjectData
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotModified
import json
import re


from .twitter.main import does_twitter_user_exist
from .text_model.config_files.config import get_text_object
from .text_model.analyzer.text_objects.text import analyze_config
from .text_model.analyzer.comparison import Comparison
from .text_model.analyzer.model.model import run_on_object
from .twitter.scrape_tweets import scrape_recent_tweets
from .text_model.analyzer.model.model import run_on_object

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
            id_match = query_set[0].id
            return Response({'status': True,
                             'id': id_match})

    @action(detail=False, url_path="compareText")
    def compare_text(self, request, pk=None):
        query_id = request.GET.get('id', None)
        query_set = TextObjectData.objects.filter(id=query_id)

        # Check that Query only returns single object with that id (supposed to be unique)
        if len(query_set) != 1:
            print(query_set)
            return HttpResponseBadRequest()
        else:
            source_model = query_set[0]
            obj = source_model.to_text_object()
            report = obj.report()

            # Grab pre_loaded tweets for comparison
            pre_loaded_texts = TextObjectData.objects.filter(source="pre_loaded")

            new_comparisons = []

            for target_model in pre_loaded_texts:
                # Check if that comparison has already been made
                comp_already_exists, new_comp = CompView.check_if_exists(source_model, target_model)

                if not comp_already_exists:
                    # Create new comparison model with each pre_loaded example.
                    new_comp = ComparisonData(label="tweet",
                                              source="analyze_text",
                                              text1=source_model,
                                              text2=target_model)
                    new_comp.save()

                new_comparisons.append(new_comp)

            # Map the model on each comparison to generate a list of the results.
            full_results = {}
            for cur_comparison in new_comparisons:
                cur_result, cur_percent = cur_comparison.run_on_model()

                full_results[cur_comparison.text2.author] = cur_percent

            # Sort the results.

            sorted_results = sorted(full_results.items(), reverse=True, key=lambda key_value_pair: key_value_pair[1])

            return Response({"report": report,
                             "result": sorted_results})


class CompView(viewsets.ModelViewSet):
    serializer_class = CompSerializer
    queryset = ComparisonData.objects.all()

    @staticmethod
    def check_if_exists(text1_ex, text2_ex):

        # Check if that comparison has already been made.

        forwards_query_set = ComparisonData.objects.filter(text1=text1_ex,
                                                           text2=text2_ex)

        backwards_query_set = ComparisonData.objects.filter(text1=text2_ex,
                                                            text2=text1_ex)

        query_set = forwards_query_set.union(backwards_query_set)

        if len(query_set) == 0:
            return False, None
        else:
            return True, query_set[0]


@api_view(['GET'])
def id_and_text_from_user(request):
    username = request.GET.get('username', None)
    existing_objects = TextObjectData.objects.filter(author=username)
    already_exists = len(existing_objects) > 0

    if not already_exists:
        tweets = scrape_recent_tweets(username)
        list_tweets = tweets["text"].tolist()
        total_text = ' '.join(list_tweets)
        data = {"label": "tweet",
                "author": username,
                "text": total_text,
                "source": "from_username"}
        return Response(data=data, status=200)
    else:
        data = {"existing_id": existing_objects[0].id}
        return Response(data=data, status=208)


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
    tweets = scrape_recent_tweets(twitter_handle) # this was changed

    # Create 'Tweet' objects
    TweetObj = get_text_object('tweet')

    # Combine all tweet text into one giant tweet.
    total_text = ' '.join(tweets)
    total_text_obj = TweetObj(total_text, raw_text=True)
    total_text_rep = total_text_obj.report()

    return Response({"tweet": total_text,
                     "report": total_text_rep,
                     })


@api_view(['GET'])
def analyze_text(request):
    text = json.loads(request.GET.get('text', None))
    label = request.GET.get('label', None)

    text_obj = get_text_object(label)
    report_1 = text_obj(text["box1"], raw_text=True, author="box1").report()
    report_2 = text_obj(text["box2"], raw_text=True, author="box2").report()
    return Response({"reports": [report_1, report_2]})


@api_view(['GET'])
def compare_raw_text(request):
    # Load in Get Params
    texts = json.loads(request.GET.get('texts', None))
    label = request.GET.get('label', None)

    text1 = texts['text1']
    text2 = texts['text2']

    text_obj = get_text_object(label)

    # Convert both to vector format to create Comparison Object
    text1_vec = text_obj(text1, raw_text=True).to_vector
    text2_vec = text_obj(text2, raw_text=True).to_vector

    comp_obj = Comparison(text1_vec, text2_vec)

    # Generate report from model
    report = run_on_object(comp_obj)
    percentage = report[1]
    verdict = report[0]

    return Response({"result": {
        "percentage": percentage,
        "verdict": verdict,
    }
    })


@api_view(['GET'])
def does_user_exist_endpoint(request):
    print(request)
    twitter_handle = request.GET.get('username', None).strip()
    twitter_username_re = re.fullmatch(r'[a-zA-Z0-9_]+', twitter_handle)
    if twitter_username_re is None:
        does_exist = False
    else:
        does_exist = does_twitter_user_exist(twitter_handle)

    return Response({"result": does_exist})



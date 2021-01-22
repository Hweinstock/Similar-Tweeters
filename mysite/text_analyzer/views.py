from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CompSerializer
from .models import ComparisonData
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json

from text_analyzer.analyzer.model.config import get_text_object
from text_analyzer.analyzer.text_objects.text import analyze_config
from text_analyzer.analyzer.comparison import Comparison

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

        return Response({'CompObject': CompObject.__dict__(),
                         'TextObject1': Text1.report(),
                         'TextObject2': Text2.report(),
                         })


@api_view(['GET'])
def headers(request):
    configs = analyze_config()
    headers = configs['headers']

    return Response({'Headers': headers})


def index(request):
    return HttpResponse("This is the bot!")

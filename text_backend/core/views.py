from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


def two_boxes(request):
    return render(request, "text_frontend/build/index.html")


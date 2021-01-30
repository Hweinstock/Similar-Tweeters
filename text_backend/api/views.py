from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["GET"])
def test(request):
    test_msg = "Hello World, it worked!"
    return Response(status=status.HTTP_200_OK, data={"data": test_msg})


def train(request):
    pass
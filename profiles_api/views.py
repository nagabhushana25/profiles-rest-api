from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Example to demonstrate the Rest Framework"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
           'Users HTTP methods as function(get, post, put, patch, delete',
           'Is similar to Django View',
           'Gives you the most control over the application',
           'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.

class App2Viwes(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse("App2 Response", safe=False)

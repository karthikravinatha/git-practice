from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.


class AppiViews(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse("App1 Response", safe=False)

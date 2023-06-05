from django.urls import path
from . import views


urlpatterns = [
    path('', views.App2Viwes.as_view())
]
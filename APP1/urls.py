from django.urls import path
from . import views


urlpatterns = [
    path('', views.AppiViews.as_view())
]
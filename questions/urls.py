# coding=utf-8
from django.conf.urls import url
from questions.views import CallbackView


urlpatterns =[
    url(r'^$', CallbackView.as_view(), name='callback'),
]
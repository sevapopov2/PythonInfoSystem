from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Добро пожаловать на страницу образовательной системы.")

def topic_detail(request, topic_id):
    return HttpResponse("You are looking at the topic %s." % topic_id)

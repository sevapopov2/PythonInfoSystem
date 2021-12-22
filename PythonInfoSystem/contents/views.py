from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    context = {'topics_list': topics_list}
    return render(request, 'contents/index.html', context)

def topic_detail(request, topic_id):
    return HttpResponse("You are looking at the topic %s." % topic_id)

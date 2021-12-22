from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    context = {'topics_list': topics_list}
    return render(request, 'contents/index.html', context)

def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("The topic doesn't exist.")
    return render(request, 'contents/topic_detail.html', {'topic': topic})

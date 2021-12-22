from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    context = {'topics_list': topics_list}
    return render(request, 'contents/index.html', context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'contents/topic_detail.html', {'topic': topic})

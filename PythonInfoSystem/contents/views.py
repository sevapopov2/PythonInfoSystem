from django.http import HttpResponse
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    output = ', '.join([t.topic for t in topics_list])
    return HttpResponse(output)

def topic_detail(request, topic_id):
    return HttpResponse("You are looking at the topic %s." % topic_id)

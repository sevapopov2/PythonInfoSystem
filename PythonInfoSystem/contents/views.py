from django.http import HttpResponse
from django.template import loader
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    template = loader.get_template('contents/index.html')
    context = {
        'topics_list': topics_list,
    }
    return HttpResponse(template.render(context, request))

def topic_detail(request, topic_id):
    return HttpResponse("You are looking at the topic %s." % topic_id)

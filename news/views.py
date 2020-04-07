from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Story


def index(request):
    latest_story_list = Story.objects.order_by('-pub_date')[:5]
    template = loader.get_template('news/index.html')
    context = {'latest_story_list': latest_story_list}
    return HttpResponse(template.render(context, request))

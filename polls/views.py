from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def get_list(request):
    json_data = serializers.serialize("json", Question.objects.all())
    return HttpResponse(json_data, content_type="application/json")

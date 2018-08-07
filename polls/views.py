from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


def question_list_temp(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def question_list(request):
    json_data = serializers.serialize("json", Question.objects.all())
    return HttpResponse(json_data, content_type="application/json")




class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

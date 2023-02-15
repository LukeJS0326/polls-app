from django.shortcuts import render
from rest_framework.response import Response
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view()
def question_list(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions,many = True)
    return Response(serializer.data)
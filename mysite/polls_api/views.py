from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Question, Choice
from polls_api.serializers import QuestionSerializer,ChoiceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer



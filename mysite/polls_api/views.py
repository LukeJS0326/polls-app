from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Question, Choice, Vote
from polls_api.serializers import QuestionSerializer,ChoiceSerializer,VoteSerializer
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
    #queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Choice.objects.filter(question_id=pk)
        

class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer

    # def post(self, request, pk, choice_pk):
    #     voter = request.data.get("voter")
    #     data = {'question': pk, 'choice': choice_pk, 'voter': voter}
    #     serializer = VoteSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


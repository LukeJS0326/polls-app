from django.shortcuts import render
from rest_framework.response import Response
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions,many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def question_detail(request,id):
    if request.method == 'GET':
        question = Question.objects.get(pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    if request.method == 'PUT':
        question = Question.objects.get(pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        question = Question.objects.get(pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
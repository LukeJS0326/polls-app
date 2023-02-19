from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/signup.html'
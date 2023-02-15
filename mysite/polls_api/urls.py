from django.urls import path, include
from .views import *

urlpatterns = [
    path('question/', question_list, name='question-list'),


]
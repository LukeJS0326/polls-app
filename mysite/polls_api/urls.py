from django.urls import path, include
from .views import *

urlpatterns = [
    #path('question/', question_list, name='question-list'),
    #path('question/<int:id>/', question_detail, name='question-detail'),

    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),


]
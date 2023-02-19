from django.urls import path
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    
    path('question/<int:pk>/choice/', ChoiceList.as_view(), name='choice-list'),
    #path("question/<int:pk>/choice/<int:choice_pk>/vote/", VoteCreate.as_view(), name="vote-create"),
    path("vote/", VoteCreate.as_view(), name="vote-create"),
    
]
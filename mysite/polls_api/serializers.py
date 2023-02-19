from rest_framework import serializers
from polls.models import Question, Choice



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question','choice_text']


class QuestionSerializer(serializers.ModelSerializer):
   choices = ChoiceSerializer(many=True, read_only=True, required=False)
   class Meta:
       model = Question
       fields = ['id', 'question_text', 'pub_date','choices']


from rest_framework import serializers
from polls.models import Question, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = ['question','choice_text','votes']


class QuestionSerializer(serializers.ModelSerializer):
   choices = ChoiceSerializer(many=True, read_only=True,required=False)
   class Meta: 
       model = Question
       fields = ['id', 'quesiton_text', 'pub_date', 'choices']

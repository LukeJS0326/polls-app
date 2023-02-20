from rest_framework import serializers
from polls.models import Question, Choice
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Question
       fields = ['id', 'question_text', 'pub_date']
       
class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'questions']
        
class RegisterSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
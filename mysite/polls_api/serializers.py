from rest_framework import serializers
from polls.models import Question, Choice

class QuestionSerializer(serializers.Serializer):
   "The fields that get serialized/deserialized"
   id = serializers.IntegerField(read_only=True)
   question_text = serializers.CharField(max_length=200)
   pub_date = serializers.DateTimeField(read_only=True)
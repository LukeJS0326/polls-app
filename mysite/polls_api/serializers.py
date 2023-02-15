from rest_framework import serializers
from polls.models import Question, Choice

class QuestionSerializer(serializers.Serializer):
   "The fields that get serialized/deserialized"
   id = serializers.IntegerField(read_only=True)
   question_text = serializers.CharField(max_length=200)
   pub_date = serializers.DateTimeField(read_only=True)

   def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)
    
   def update(self, instance, validated_data):
       """
       Update and return an existing `Question` instance, given the validated data.
       """
       instance.question_text = validated_data.get('question_text', instance.question_text)
       instance.save()
       return instance

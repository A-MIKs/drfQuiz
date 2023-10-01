from .models import *
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["title"]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "answer_text", "is_right"]

class RandomQuestionSerializer(serializers.ModelSerializer):
    #answers = serializers.StringRelatedField(many=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ["title", "answers"]

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ["quiz","title", "answers"]

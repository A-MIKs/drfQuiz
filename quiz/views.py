from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class QuizList(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
    
class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from alunos.models import Aluno
from alunos.serializers import AlunoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

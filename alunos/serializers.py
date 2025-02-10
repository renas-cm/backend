from rest_framework.serializers import ModelSerializer
from alunos.models import Aluno

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
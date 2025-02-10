from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nome} - {self.idade} - {self.email} - {self.telefone}"

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome}"
    
class Endereço(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    cep = models.IntegerField()
    
from django.contrib import admin

from .models import Aluno, Estado, Cidade, Endereço

admin.site.register(Aluno)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereço)

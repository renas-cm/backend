# Generated by Django 4.2.18 on 2025-02-10 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_cidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cidade',
            old_name='Estado',
            new_name='estado',
        ),
        migrations.CreateModel(
            name='Endereço',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField(verbose_name=5)),
                ('cep', models.IntegerField(verbose_name=8)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.cidade')),
            ],
        ),
    ]

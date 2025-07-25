# Generated by Django 5.2.4 on 2025-07-09 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('assembleia', 'Assembleia'), ('reuniao', 'Reunião'), ('curso', 'Curso'), ('palestra', 'Palestra'), ('confraternizacao', 'Confraternização'), ('outro', 'Outro')], default='reuniao', max_length=20)),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('andamento', 'Em Andamento'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], default='agendado', max_length=20)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('local', models.CharField(max_length=200)),
                ('endereco', models.TextField()),
                ('capacidade_maxima', models.PositiveIntegerField(blank=True, null=True)),
                ('inscricao_obrigatoria', models.BooleanField(default=False)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='eventos/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_organizados', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['data_inicio'],
            },
        ),
        migrations.CreateModel(
            name='InscricaoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('presente', models.BooleanField(default=False)),
                ('observacoes', models.TextField(blank=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to='events.evento')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscrição em Evento',
                'verbose_name_plural': 'Inscrições em Eventos',
                'ordering': ['data_inscricao'],
                'unique_together': {('evento', 'participante')},
            },
        ),
    ]

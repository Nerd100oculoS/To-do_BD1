# Generated by Django 4.1 on 2023-06-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "password",
                    models.CharField(
                        db_column="senha", max_length=128, verbose_name="password"
                    ),
                ),
                (
                    "nome_usuario",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=60)),
                ("telefone", models.IntegerField()),
                ("email", models.CharField(max_length=60)),
            ],
            options={"db_table": "Usuario", "managed": False,},
        ),
        migrations.CreateModel(
            name="Convite",
            fields=[
                ("id_convite", models.AutoField(primary_key=True, serialize=False)),
                ("aceito", models.IntegerField()),
            ],
            options={"db_table": "Convite", "managed": False,},
        ),
        migrations.CreateModel(
            name="ListaDeTarefas",
            fields=[
                ("id_lista", models.AutoField(primary_key=True, serialize=False)),
                ("nome_descritivo", models.CharField(max_length=60)),
                ("data_hora_criacao", models.DateTimeField()),
                ("data_hora_modificacao", models.DateTimeField()),
                ("responsavel_modificacao", models.CharField(max_length=20)),
            ],
            options={"db_table": "Lista_de_Tarefas", "managed": False,},
        ),
        migrations.CreateModel(
            name="Tarefas",
            fields=[
                ("id_tarefa", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(max_length=100)),
                ("data_cadastro", models.DateTimeField()),
                ("data_vencimento", models.DateTimeField(blank=True, null=True)),
                ("tarefa_concluida", models.IntegerField()),
            ],
            options={"db_table": "Tarefas", "managed": False,},
        ),
    ]

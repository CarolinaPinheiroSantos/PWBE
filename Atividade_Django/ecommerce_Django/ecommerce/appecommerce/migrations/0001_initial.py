# Generated by Django 5.1.6 on 2025-02-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
    ]

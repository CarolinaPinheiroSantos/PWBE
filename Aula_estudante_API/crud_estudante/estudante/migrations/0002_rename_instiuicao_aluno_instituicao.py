# Generated by Django 5.1.7 on 2025-03-13 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='instiuicao',
            new_name='instituicao',
        ),
    ]

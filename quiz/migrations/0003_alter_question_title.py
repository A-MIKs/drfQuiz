# Generated by Django 4.2.4 on 2023-08-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='New Question', max_length=255, verbose_name='Question Title'),
        ),
    ]

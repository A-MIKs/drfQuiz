# Generated by Django 4.2.4 on 2023-08-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title'),
        ),
    ]

# Generated by Django 3.0 on 2020-12-27 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20201227_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat_message',
            name='chat_box',
        ),
    ]

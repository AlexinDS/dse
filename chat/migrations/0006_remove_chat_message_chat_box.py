# Generated by Django 3.0 on 2020-12-27 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chat_message_chat_box'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat_message',
            name='chat_box',
        ),
    ]

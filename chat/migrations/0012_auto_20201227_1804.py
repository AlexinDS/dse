# Generated by Django 3.0 on 2020-12-27 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20201227_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_message',
            name='chat_box',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='chat.Chat_box'),
        ),
    ]

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Chat_box(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Chat_message(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    chat_box = models.TextField()#ForeignKey('Chat_box',on_delete=models.CASCADE)

    def publish(self):
        self.date = timezone.now()
        self.save()

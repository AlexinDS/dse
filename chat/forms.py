from django import forms
from .models import Chat_box, Chat_message

class Chat_boxForm(forms.ModelForm):
    content = forms.CharField(label="Info", max_length=45)
    class Meta:
        model = Chat_box
        fields = ('title', 'content','category')

class Chat_messageForm(forms.ModelForm):
    content = forms.CharField(label="Message ", max_length=35)
    chat_box = Chat_box
    class Meta:
        model = Chat_message
        fields = ('content',)

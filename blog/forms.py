from django import forms
from .models import Post

class ContactForm(forms.Form):
    topic = forms.CharField(max_length=100)
    text = forms.CharField(label='Text')
    sender = forms.EmailField(label="Your e-mail adress")

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = Post
        fields = ('title', 'content','category')

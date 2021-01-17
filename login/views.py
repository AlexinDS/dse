from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def Login(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

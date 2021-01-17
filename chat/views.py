from django.shortcuts import render, get_object_or_404, redirect
from chat.models import Chat_box, Chat_message
from .forms import Chat_boxForm, Chat_messageForm
from django.contrib.auth import logout
from django.utils import timezone
from login.views import Login


def Chat_Home(request):
    all_chat = Chat_box.objects.all()
    return render(request, 'chat_home.html', {'all_chat': all_chat})

def Chat_Read(request, id):
    now = timezone.now()
    chat = get_object_or_404(Chat_box, id=id)
    all_message = Chat_message.objects.filter(chat_box=chat.id).order_by('-date')
    nb_message = all_message.count()
    if request.method == "POST":
        form = Chat_messageForm(request.POST) #or None, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.date = timezone.now()
            message.chat_box = chat.id
            chat = get_object_or_404(Chat_box, id=id)
            all_message = Chat_message.objects.filter(chat_box=chat.id).order_by('-date')
            nb_message = all_message.count() + 1
            message.save()
        return render(request, 'chat_read.html', {'chat': chat, 'all_message': all_message,'nb_message':nb_message,'form':form})
    else:
        form = Chat_messageForm()
    return render(request, 'chat_read.html', {'chat':chat, 'all_message':all_message, 'nb_message':nb_message, 'form': form})

def Logout(request):
    logout(request)
    return redirect(Login)


def Chat_New(request):
    if request.method == "POST":
        form = Chat_boxForm(request.POST) #or None, request.FILES)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.date = timezone.now()
            chat.save()
        return redirect(Chat_Home)
    else:
        form = Chat_boxForm()
    return render(request, 'chat_new.html', {'form': form})

def Chat_Edit(request, id):
    chat = get_object_or_404(Chat_box, id=id)
    if request.method == "POST":
        form = Chat_boxForm(request.POST, instance=chat) #or None, request.FILES,
        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.date = timezone.now()
            chat.save()
        return redirect(Chat_Read, id)
    else:
        form = Chat_boxForm(instance=chat)
    return render(request, 'chat_edit.html', {'form': form, 'chat': chat})

def Chat_delete(request, id):
    chat = get_object_or_404(Chat_box, id=id)
    all_message = Chat_message.objects.filter(chat_box=chat.id)
    if request.user == chat.author or request.user.is_superuser:
        Chat_box.objects.get(id=id).delete()
        all_message.delete()
    return redirect(Chat_Home)

##################################################################################################

def bad_request(request, exception):
    return render(request, 'bad_request.html', locals())

def permission_denied(request, exception):
    return render(request, 'permission_denied.html', locals())

def page_not_found(request, exception):
    return render(request, 'page_not_found.html', locals())

def server_error(request):
    return render(request, 'server_error.html', locals())

##################################################################################################

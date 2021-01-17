from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import ContactForm, PostForm
from django.contrib.auth import logout
from django.utils import timezone
from login.views import Login


def Date(request):
    return render(request, 'date.html', {'date': datetime.now()})

def Addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request, 'addition.html', locals())

def Blog_Home(request):
    all_post = Post.objects.all()
    return render(request, 'blog_home.html', {'all_post': all_post})

def Blog_Read(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_read.html', {'post':post})

def Contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        topic = form.cleaned_data['topic']
        text = form.cleaned_data['text']
        sender = form.cleaned_data['sender']
        sending = True

    return render(request, 'contact.html', locals())


def Logout(request):
    logout(request)
    return redirect(Login)

def Blog_New(request):
    if request.method == "POST":
        form = PostForm(request.POST) #or None, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
        return render(request, 'blog_read.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'blog_new.html', {'form': form})

def Blog_Edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #or None, request.FILES,
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
#            if User.is_authentified and User.username == article.auteur:
 #               article.auteur.is_connected = True
        return render(request, 'blog_read.html', {'post': post})
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_edit.html', {'form': form, 'post': post})

def Blog_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        Post.objects.get(id=id).delete()
    return redirect(Blog_Home)


###################################################################################################
def bad_request(request, exception):
    return render(request, 'bad_request.html', locals())

def permission_denied(request, exception):
    return render(request, 'permission_denied.html', locals())

def page_not_found(request, exception):
    return render(request, 'page_not_found.html', locals())

def server_error(request):
    return render(request, 'server_error.html', locals())

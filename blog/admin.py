from django.contrib import admin
from blog.models import Category as Categories, Post

admin.site.register(Categories)
admin.site.register(Post)

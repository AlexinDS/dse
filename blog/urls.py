from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog_Home, name='blog_home'),
    path('p/<int:id>', views.Blog_Read, name='blog_read'),
    path('c/', views.Contact, name='contact'),
    path('logout/', views.Logout, name='logout'),
    path('n/', views.Blog_New, name='new_post'),
    path('e/<int:id>', views.Blog_Edit, name='edit_post'),
    path('r/<int:id>', views.Blog_delete, name='delete_post'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Chat_Home, name='chat_home'),
    path('c/<int:id>', views.Chat_Read, name='chat_read'),
    path('logout/', views.Logout, name='logout'),
    path('n/', views.Chat_New, name='new_chat'),
    path('e/<int:id>', views.Chat_Edit, name='edit_chat'),
    path('r/<int:id>', views.Chat_delete, name='delete_chat'),
]

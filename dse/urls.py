from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('', include('login.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]

handler400 = 'blog.views.bad_request'
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

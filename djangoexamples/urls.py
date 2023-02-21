from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('projects/', include('projects.urls', namespace='projects'))
]

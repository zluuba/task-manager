from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', views.users, name='users'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', include('task_manager.users.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

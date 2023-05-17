from django.urls import path, include
from django.contrib import admin

from task_manager.users.views import UserLoginView, UserLogoutView
from task_manager.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

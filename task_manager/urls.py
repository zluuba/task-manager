from django.contrib import admin
from django.urls import path, include
from task_manager.users.views import UserLoginView, UserLogout
from task_manager.views import HomeView, test_case


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    # path('labels/', include('task_manager.labels.urls')),
    # path('tasks/', include('task_manager.tasks.urls')),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('test/', test_case)
]

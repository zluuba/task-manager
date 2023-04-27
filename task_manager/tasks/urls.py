from task_manager.tasks import views
from django.urls import path

urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', views.TaskView.as_view(), name='task'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]

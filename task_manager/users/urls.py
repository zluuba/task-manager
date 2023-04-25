from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('create/', views.UserFormCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', views.UserFormUpdateView.as_view(), name='users_update'),
    path('<int:pk>/delete/', views.UserFormDeleteView.as_view(), name='users_delete'),
]

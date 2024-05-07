from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('<int:todo_id>/update/', views.todo_update, name='todo_update'),
    path('<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
    path('accounts/login/', views.login_view, name="login_view")
]   
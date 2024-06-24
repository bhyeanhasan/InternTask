# urls.py
from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:project_id>/task/', TaskListCreateView.as_view(), name='task-list-create'),
]

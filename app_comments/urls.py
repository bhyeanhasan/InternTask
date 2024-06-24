# urls.py
from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('<int:task_id>/comment/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
]

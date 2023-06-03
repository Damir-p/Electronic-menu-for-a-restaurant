from django.urls import path
from apps.blog.views import PostsView, PostDetailView, AboutView

urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'),    
    path('about/', AboutView.as_view(), name='about'),
]
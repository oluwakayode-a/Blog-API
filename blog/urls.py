from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name=None),
    path('create/', views.PostCreateView.as_view(), name=None),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name=None),
    path('categories/', views.CategoryListView.as_view(), name=None),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name=None),
    path('comment', views.CommentCreateView.as_view(), name=None)
]
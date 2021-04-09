from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='_post'),
    path('create/', views.PostCreate.as_view(), name='_create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='_delete'),
    path('like/', views.likes, name='likes'),
    ]

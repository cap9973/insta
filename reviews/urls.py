from django.urls import path
from . import views

app_name='reviews'
urlpatterns = [
    path('create/<int:pk>/', views.PostCreateReView.as_view(), name='review_create'),
    path('delete/<int:pk>/', views.PostDeleteReview.as_view(), name='review_delete'),
    path('list/<int:pk>/', views.ReViewList.as_view(), name='review_list'),
]
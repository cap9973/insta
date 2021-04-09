from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='users'
urlpatterns = [

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register')
]
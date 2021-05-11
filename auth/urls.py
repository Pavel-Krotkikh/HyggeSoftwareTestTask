from django.urls import path
from auth import views


urlpatterns = [
    path('register/', views.auth_register),
    path('login/', views.auth_login),
    path('logout/', views.auth_logout),
]

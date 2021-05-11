from django.urls import path, include
from users import views

urlpatterns = [
    path('/', views.user_list),
    path('me/', views.user_detail),

    path('register/', views.user_register),
    path('auth/', views.user_auth),
    path('logout/', views.user_logout),

    path('friends/', views.friends),
    path('<int:user_id>/friend_request/', views.friend_request),
    path('<int:user_id>/friend_request/accept/', views.friend_accept),
]

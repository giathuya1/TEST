from django.urls import path, include
from .views import (
    UserRegisterView,
    UserLoginView,  
    UserLogoutView,
    UserProfileView,
    UserUpdateView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),      
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
    
]
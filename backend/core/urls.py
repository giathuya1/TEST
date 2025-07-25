from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('users/', include('apps.users.urls')), #Đường dẫn đến app users

]
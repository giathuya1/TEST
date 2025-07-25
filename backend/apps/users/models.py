from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    """
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)   
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=10,blank=True,)
    
    USER_TYPE_Choices = [
        ('student', 'Sinh viên'),
        ('lecturer', 'Giảng viên'),
        ('external', 'Khách'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'), 
    ]
    
    gender_type = models.CharField(
        max_length=10,
        choices = GENDER_CHOICES
    )
    
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_Choices,    
        default='external',
    )
    
    
    MIT_USER = models.CharField(
        max_length=10,
        blank=True,
        unique=True,
        null=True,
    )
    
    
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    def clean(self):
        """
        Custom clean method to ensure that the email field is unique.
        """
        super().clean()
        
        if self.user_type in ['student', 'lecturer'] and not self.MIT_USER:
            raise ValidationError({'MIT_USER': 'Đây là trường dữ liệu dành cho MITER.'})
        
        if User.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': 'Email must be unique.'})
        
       
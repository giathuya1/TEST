from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta :
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 
            'user_type','password1','password2',
            'phone', 'address' , 'MIT_USER', 'gender_type'
        )
        
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        mit_user = cleaned_data.get("MIT_USER")
        phone_user = cleaned_data.get("phone")
        if user_type in ['student', 'lecturer'] and not mit_user:
            self.add_error("MIT_USER", "Chỉ có MITER mới có trường này")
        if not phone_user.isdigit() and len(phone_user) != 10:
            ValidationError("Số điện thoại phải là số và có độ dài 10 ký tự")
        return cleaned_data
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 
            'user_type', 'phone', 'address', 'MIT_USER'
        )
        
        
        
        
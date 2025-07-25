from django.contrib.auth.admin import UserAdmin
from apps.users.models import User
from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the User model.
    """
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'phone', 'MIT_USER','gender_type')
    list_filter = ('is_active', 'MIT_USER', 'user_type','gender_type')

    
    #Các trường sau sẽ được hiển thị trong form chỉnh sửa người dùng
    fieldsets = UserAdmin.fieldsets + (
        (None, {'field' : ('email', 'phone', 'user_type',) }),
        ('Additional Info', {'fields': ('MIT_USER',)}),
    )
    
    # Các trường sau sẽ được hiển thị trong form tạo người dùng
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'MIT_USER')}),
        
    )
    
    search_fields = ('username', 'email')
    ordering = ('username',)
    
# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
    
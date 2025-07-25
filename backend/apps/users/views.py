from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib import messages as message

class UserRegisterView(CreateView):
    """
    View for user registration.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        """
        Override to set the user type to 'external' by default.
        """
        message.success(self.request, "Đăng ký thành công")
        return super().form_valid(form)

class UserLoginView(LoginView):
    """
    View for user login.
    """
    template_name = 'users/login.html'
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True
    def form_valid(self, form):
        """
        Override to display a success message on successful login.
        """
        message.success(self.request, "Đăng nhập thành công")
        return super().form_valid(form)
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'student':
            return reverse_lazy('student_dashboard')
        elif user.user_type == 'lecturer':
            return reverse_lazy('lecturer_dashboard')
        return reverse_lazy('dashboard')
    
class UserLogoutView(LogoutView):
    """
    View for user logout.
    """
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        """
        Override to display a success message on logout.
        """
        message.success(request, "Đăng xuất thành công")
        return super().dispatch(request, *args, **kwargs)
    
class UserProfileView(LoginRequiredMixin,DetailView):
    """
    View for displaying user profile.
    """
    model = User
    template_name = 'users/profile.html'
    
    def get_object(self, queryset=None):
        """
        Override to get the current logged-in user.
        """
        return self.request.user
 
    
class UserUpdateView(LoginRequiredMixin,UpdateView):      
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('profile')
    def get_object(self, queryset=None):
        """
        Override to get the current logged-in user.
        """
        return self.request.user
    

    
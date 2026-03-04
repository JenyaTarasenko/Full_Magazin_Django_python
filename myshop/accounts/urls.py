from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.MyLogoutView.as_view(next_page='/'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/change_password/', views.change_password, name='change_password'),
    #страничка успешного регистрации редирект после регистрации
    path('successful/', TemplateView.as_view(template_name='accounts/successful.html'), name='successful'),
]
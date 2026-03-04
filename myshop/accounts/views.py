from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmailSignupForm, PasswordChangeForm


# как это работает когда зарегестрирован и можно выйти 
# и джанго тебя забудет потом нужно ввести заново логин и пароль    
class MyLogoutView(LogoutView):
    http_method_names = ['get', 'post']  # разрешаем GET

# Регистрация
def signup(request):
    if request.method == 'POST':
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:successful')
        else:
            print(form.errors)  # <--- вывод ошибок в консоль
    else:
        form = EmailSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Профиль
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# Смена пароля
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # чтобы не выкинуло после смены
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

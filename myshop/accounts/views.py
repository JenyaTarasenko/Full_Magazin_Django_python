# from django.shortcuts import render, redirect
# from django.contrib.auth import login, update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import LoginView, LogoutView
# from .forms import EmailSignupForm, PasswordChangeForm


# # как это работает когда зарегестрирован и можно выйти 
# # и джанго тебя забудет потом нужно ввести заново логин и пароль    
# class MyLogoutView(LogoutView):
#     http_method_names = ['get', 'post']  # разрешаем GET

# # Регистрация
# def signup(request):
#     if request.method == 'POST':
#         form = EmailSignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('accounts:successful')
#         else:
#             print(form.errors)  # <--- вывод ошибок в консоль
#     else:
#         form = EmailSignupForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# # Профиль
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')

# # Смена пароля
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # чтобы не выкинуло после смены
#             return redirect('accounts:profile')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/change_password.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# функция регистрации  после регистрации нужно ввести имя пароль и подтверждение пароля
def signup_view(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("accounts:login")

    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})



# функция входа после входа вывод имени 
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")  # главная магазина
        else:
            messages.error(request, "Неверное имя пользователя или пароль")

    return render(request, "accounts/login.html")


# функция выхода просто выходишь из аккаунта
def logout_view(request):
    logout(request)
    return redirect("shop:product_list")
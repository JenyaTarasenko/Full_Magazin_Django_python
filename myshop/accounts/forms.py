# from django import forms
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from django.contrib.auth.models import User

# # Регистрация по email
# class EmailSignupForm(UserCreationForm):
#     email = forms.EmailField(label='Email')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.username = self.cleaned_data['email']  # используем email как username
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(label="Имя")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # проверка username
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует")

        return username

    # проверка email
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется")

        return email
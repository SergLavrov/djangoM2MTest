from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
        validators=[
        MinLengthValidator(5, message='Минимум 5 символов'),
        MaxLengthValidator(10, message='Максимум 10 символов'),
        ]
    )
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2: self.add_error('password2', 'Пароли не совпадают !')
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise forms.ValidationError('Имя пользователя не должно содержать пробелов !')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует !')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким Email уже существует !')
        return email

    # def clean_confirm_password(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError('Пароли не совпадают !')
    #     return password2

    # def user_exists(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Пользователь с таким именем уже существует !')
    #     return username

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


# ВАРИАНТ "C"
# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class AuthenticationForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Имя пользователя', required=True)
#     password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)
#
#     def username_password(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not authenticate(username=username, password=password):
#             raise forms.ValidationError('Неверное имя пользователя или пароль !')
#         return username, password


# class LoginForm(forms.ModelForm):  # Форма логина
#
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f"Пользователь с логином {username} не найден")
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError("Неверный пароль")
#         return self.cleaned_data
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']

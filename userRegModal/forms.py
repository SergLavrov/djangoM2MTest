from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

# class RegisterForm(forms.ModelForm):
#     username = forms.CharField(validators=[
#         MinLengthValidator(5, message='Минимум 5 символов'),
#         MaxLengthValidator(10, message='Максимум 10 символов'),
#     ])
#     email = forms.EmailField()
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#
#     def clean_confirm_password(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 != password2:
#             raise forms.ValidationError('Пароли не совпадают !')
#         return password2
#
#     def user_exists(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError('Пользователь с таким именем уже существует !')
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError('Пользователь с таким Email уже существует !')
#         return email
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if ' ' in username:
#             raise forms.ValidationError('Имя пользователя не должно содержать пробелов !')
#         return username
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'confirm_password', 'email']




# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Имя пользователя')
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# ВАРИАНТ "C"
# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class AuthenticationForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)

    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    # username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    # password = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    # )
    #
    # error_messages = {
    #     "invalid_login": _(
    #         "Please enter a correct %(username)s and password. Note that both "
    #         "fields may be case-sensitive."
    #     ),
    #     "inactive": _("This account is inactive."),
    # }


# class LoginForm(forms.ModelForm):
# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         # 'class': 'form-control',
#         'placeholder': 'Введите имя пользователя'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         # 'class': 'form-control',
#         'placeholder': 'Введите пароль'
#     }))


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
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

from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class RegisterForm(forms.ModelForm):
    username = forms.CharField(validators=[
        MinLengthValidator(5, message='Минимум 5 символов'),
        MaxLengthValidator(10, message='Максимум 10 символов'),
    ])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return confirm_password

    def user_exists(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким Email уже существует')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

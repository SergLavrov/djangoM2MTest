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

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
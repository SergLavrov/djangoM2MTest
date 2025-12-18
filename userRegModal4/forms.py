from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Создадим "кастомную форму" для регистрации, т.е. добавим еще свои поля в форму UserCreationForm:


class UserAddFieldForm(UserCreationForm):     # наследуемся UserCreationForm (см. в файле views.py)
    email = forms.EmailField(required=True)   # required - значит поле обязательно для заполнения!

    class Meta:
        model = User  # импортируем - import User из коробки Django
        fields = ("username", "password1", "password2", "email")

    # Проверка на email со стороны браузера :
    # - example (... отсутствует символ @)
    # - example@ (Введите часть адреса после символа @. Адрес ... неполный!)

    # Проверка на email со стороны django:
    # - example@gmail (Введите правильный адрес электронной почты.)

    def clean_email(self):                                       # Проверка на email также со стороны сервера:
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email уже существует!")
        return email

    def save(self, commit=True):
        user = super(UserAddFieldForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]                  # добавляем email
        if commit:
            user.save()
        return user

    # Пояснение - в этой функции мы переопределяем стандартный метод "save",
    # (из views.py -> def form_valid(self, form) --> form.save() --> здесь для него ставим: save(commit=False));
    # получаем из cleaned_data["email"] и сохраняем пользователя в базу данных, но уже с email !!!
    # И возвращаем его --> return user.

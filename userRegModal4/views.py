from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import UserAddFieldForm  # импортируем нашу "кастомную форму" для регистрации из forms.py


def home_page(request):
    return render(request, 'userRegModal4/home4.html')


def reg_success(request):
    return render(request, 'userRegModal4/reg_success.html')


# Вариант 1.1 - через "кастомную форму" UserAddFieldForm (добавили поле email при регистрации)
class RegisterFormView(FormView):
    form_class = UserAddFieldForm   # Используем нашу "кастомную форму" для регистраци из forms.py
    template_name = 'userRegModal4/register_form4.html'

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'html': html})
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string(self.template_name, {'form': form}, request=self.request)
            return JsonResponse({'success': False, 'html': html})
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('home')
        # return reverse('reg_success')


''' Вариант 1.2 При регистрации заполняем только: username, password1, password2 !!! '''
# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     template_name = 'userRegModal4/register_form4.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.get_form()
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             html = render_to_string(self.template_name, {'form': form}, request=request)
#             return JsonResponse({'html': html})
#         return super().get(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         form.save()
#         if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             return JsonResponse({'success': True})
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             html = render_to_string(self.template_name, {'form': form}, request=self.request)
#             return JsonResponse({'success': False, 'html': html})
#         return super().form_invalid(form)
#
#     def get_success_url(self):
#         return reverse('home')

'''
    1. Имортируем его - from django.contrib.auth.forms import UserCreationForm
    2. UserCreationForm - это стандартный класс для создания форм, который представляет Django из своей "КОРОБКИ"
    для стандартной ВАЛИДАЦИИ вводимых данных:
    - Обязательное поле.Не более 150 символов.Только буквы, цифры и символы @ /./ + / - / _.
    - Пароль не должен быть слишком похож на другую вашу личную информацию.
    - Ваш пароль должен содержать как минимум 8 символов.
    - Пароль не должен быть слишком простым и распространенным.
    - Пароль не может состоять только из цифр.
    - Ошибка: Пользователь с таким именем уже существует.
    - Ошибка: Введенный пароль слишком похож на имя пользователя.
    - Подтверждение пароля: Ошибка - Пароли не совпадают.
    - Подтверждение пароля: Ошибка - Для подтверждения введите, пожалуйста, пароль ещё раз.
'''

# Вариант 1.3 - стандартная регистрация пользователя: username, password1, password2
# class RegisterFormView(FormView):
#
#     form_class = UserCreationForm  # Элементарная форма для регистрации!
#
#     template_name = 'userRegModal4/register_form4.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('home')
#
#     def form_invalid(self, form):
#         return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'userRegModal4/login_form4.html'
    # success_url = '/reg/home/'

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'html': html})
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"success": True})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            html = render_to_string(self.template_name, {"form": form}, request=self.request)
            return JsonResponse({"success": False, "html": html})
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('home')


# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'userRegModal4/login_form4.html'
#     success_url = '/reg/home/'
#
#     def form_valid(self, form):
#         user = form.get_user()
#         login(self.request, user)
#
#         if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
#             # Возвращаем пустую форму без ошибок (успех)
#             html = render_to_string(self.template_name, {"form": self.form_class()})
#             return JsonResponse({"success": True, "html": html})
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
#             html = render_to_string(self.template_name, {"form": form})
#             return JsonResponse({"success": False, "html": html})
#         return super().form_invalid(form)

# а)
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('home')

    # унаследован от класса View
    # импортируем View - from django.views import View
    # from django.contrib.auth import logout

# б)
def logout_user(request):   # можно сделать без класса представления - class LogoutView(View):
    logout(request)
    return redirect('home')
    # return HttpResponseRedirect(reverse('home'))   # или так!

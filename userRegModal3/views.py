from django.forms import fields
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterForm
# from .forms import LoginForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.urls import reverse_lazy
# from .forms import LoginUserForm

'''
Ajax (Asynchronous JavaScript and XML) — это технология, позволяющая обновлять информацию на странице 
без ее полного перезагрузки. Это особенно важно в современном веб-разработке, где пользователи 
ожидают мгновенных результатов и отзывчивых интерфейсов.
Источник: https://funday24.driverlib.ru/ajax-form-on-error
'''


def home_page(request):
    return render(request, 'userRegModal3/home3.html')

# def prod_list(request):
#     return render(request, 'userRegModal/prod_list.html')

'''
КЛЮЧЕВОЙ МОМЕНТ: Django по умолчанию не хранит пароли в БД. Поэтому вам нужно их хешировать самостоятельно.

Используйте UserCreationForm или метод create_user.

Никогда не делайте User.objects.create(username=..., password=...), иначе пароль сохранится в базе в открытом виде.
Правильно: используем create_user, он сам вызывает set_password()
        user = User.objects.create_user(username=username, password=password)

form.save() внутри UserCreationForm автоматически вызывает set_password(), и пароль попадает в БД в хешированном 
виде (алгоритм по умолчанию — PBKDF2 с SHA256).
Таким образом, ваш AJAX‑код останется прежним, а серверная часть будет гарантированно хешировать пароли.
'''

def reg_form(request):
    if request.method == 'GET':
        form = RegisterForm()
        html = render_to_string('userRegModal3/register_form3.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # создаём пользователя
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            return JsonResponse({'success': True})
        else:
            html = render_to_string('userRegModal3/register_form3.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})


def login_form(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        html = render_to_string('userRegModal3/login3.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # авторизация пользователя
            user = form.get_user()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            html = render_to_string('userRegModal3/login3.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})


def logout_user(request):
    logout(request)
    return redirect('home')
    # return HttpResponseRedirect(reverse('home'))


# # 1 Вар
# # def reg_form(request):
# #     if request.method == 'POST':
# #         form = RegisterForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             # return HttpResponse("Регистрация успешна!")  # AJAX получит этот ответ
# #             # messages.success(request, 'Registration completed successfully! You can login to the site!')
# #             return HttpResponseRedirect(reverse('home'))
# #             # return JsonResponse({'success': True})
# #             # return render(request, 'success.html')  # Успешная регистрация
# #         else:
# #             return render(request, 'userRegModal/register_form3.html', {'form': form})  # Ошибки
# #     else:
# #         form = RegisterForm()
# #     return render(request, 'userRegModal/register_form3.html', {'form': form})
#
#
# # def login_form(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(request, data=request.POST)
# #         if form.is_valid():
# #             user = form.get_user()
# #             login(request, user)
# #             return redirect('home')  # Замените 'home' на URL вашей домашней страницы
# #     else:
# #         form = AuthenticationForm()
# #     return render(request, 'userRegModal/login3.html', {'form': form})
#
#
# def login_form(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#         # username = request.POST.get('username')
#         # password = request.POST.get('password')
#         # user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("OK")
#                 # return HttpResponseRedirect(reverse('home'))
#                 # return HttpResponseRedirect(reverse('profile'))
#
#         # < !-- если пользователь с таким именем/паролем НЕ существует -->
#         # return HttpResponseRedirect(reverse('home'))
#
#     else:
#         form = LoginForm()
#     return render(request, 'userRegModal/login3.html', {'form': form})
#         # return HttpResponseRedirect(reverse('home'))



# def login_form(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  # Redirect to a home page or dashboard
#     else:
#         form = LoginForm()
#     return render(request, 'userRegModal/login3.html', {'form': form})


# Для ВАРИАНТа "B" - см javascript в login3.html
# def login_form(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             # Возвращаем пустой ответ без ошибок → JS перезагрузит страницу
#             # messages.success(request, 'You have successfully login to the site!')
#             # return HttpResponseRedirect(reverse('home'))
#             # return HttpResponse("OK")
#             return JsonResponse({'success': True})
#         else:
#             # Ошибки: рендерим форму заново с сообщениями
#             html = render_to_string("userRegModal/login3.html", {"form": form}, request)
#             return JsonResponse({'success': False, 'html': html})
#             # return render(request, "userRegModal/login3.html", {"form": form})
#     else:
#         # GET: просто отрисовать форму
#         form = AuthenticationForm()
#         return render(request, "userRegModal/login3.html", {"form": form})


# def custom_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         # form = CustomLoginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, 'userRegModal/login_success.html')  # Успешная авторизация
#                     # return HttpResponseRedirect(reverse('home'))
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#         else:
#             return render(request, 'userRegModal/login3.html', {'form': form})
#     else:
#         form = CustomLoginForm()
#     return render(request, 'userRegModal/login3.html', {'form': form})


# Для ВАРИАНТа "А" - см javascript в login3.html
# def login_form(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return JsonResponse({"success": True})
#         else:
#             # Ошибки: возвращаем JSON с текстом ошибок
#             return JsonResponse({
#                 "success": False,
#                 "errors": form.errors.as_json()
#             })
#     else:
#         # GET: можно вернуть пустой JSON или HTML формы
#         form = AuthenticationForm()
#         return JsonResponse({
#             "form_html": render(request, "userRegModal/login3.html",
#                                 {"form": form}).content.decode("utf-8")
#         })


# def login_form(request):
#     form = AuthenticationForm(data=request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)  # Проверяем учетные данные
#             if user is not None:
#                 login(request, user)     # Выполняем вход
#                 return redirect('home')  # Перенаправляем на главную страницу
#         else:
#             return render(request, 'userRegModal/login3.html', {'form': form})
#     else:
#         form = AuthenticationForm()
#     return render(request, 'userRegModal/login3.html', {'form': form})


# def login_form(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home')  # Перенаправляем на главную страницу
#                     # return HttpResponse('Authenticated successfully')
#                 # messages.success(request, 'Login completed successfully!')
#                 # return HttpResponseRedirect(reverse('home'))
#                 #     return JsonResponse({'success': True})
#                 else:
#                     return HttpResponse('Disabled account')
#                 else:
#                     # Ошибки: рендерим форму заново с сообщениями
#                     html = render_to_string("userRegModal/login3.html", {"form": form}, request)
#                     return JsonResponse({'success': False, 'html': html})
#                 # return HttpResponse('Invalid login')
#                 # return render(request, 'userRegModal/login3.html', {'form': form})  # Ошибки
#         else:
#             form = LoginForm()
#             return render(request, 'userRegModal/login3.html', {'form': form})


'''
ХОРОШИЙ ПРИМЕР:
https://pocoz.gitbooks.io/django-v-primerah/content/glava-4-sozdanie-social-website/ispolzovanie-django-authentication-framework/sozdanie-log-in-view.html

https://ru.stackoverflow.com/questions/1602265/%d0%9a%d0%b0%d0%ba-%d0%be%d1%82%d0%be%d0%b1%d1%80%d0%b0%d0%b6%d0%b0%d1%82%d1%8c-%d1%84%d0%be%d1%80%d0%bc%d1%83-%d0%b2-%d0%bc%d0%be%d0%b4%d0%b0%d0%bb%d1%8c%d0%bd%d0%be%d0%bc-%d0%be%d0%ba%d0%bd%d0%b5-%d0%bf%d1%80%d0%b8-%d0%b2%d0%b2%d0%be%d0%b4%d0%b5-%d0%bd%d0%b5%d0%ba%d0%be%d1%80%d1%80%d0%b5%d0%ba%d1%82%d0%bd%d1%8b%d1%85-%d0%b4%d0%b0%d0%bd%d0%bd%d1%8b%d1%85
'''

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({"success": True})
#         else:
#             return JsonResponse({"success": False, "error": "Неверные данные для входа"})
#
#     return JsonResponse({"success": False, "error": "Неверный метод запроса"})




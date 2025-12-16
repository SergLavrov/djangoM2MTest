from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
from .forms import LoginForm


def home_page(request):
    return render(request, 'userRegLog/home.html')


# def reg_form(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#             # return redirect('home')   # или HttpResponse('')
#             # messages.success(request, 'Вы успешно зарегистрированы!')
#         else:
#             return render(request, 'userRegLog/home.html', {'form': form})
#     else:
#         form = RegisterForm()
#         return render(request, 'userRegLog/home.html', {'form': form})


# 1 Вариант
def reg_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return render(request, 'userRegLog/reg_form2.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'userRegLog/reg_form2.html', {'form': form})


# 2 Вариант через UserCreationForm
# def reg_form(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return render(request, 'userRegLog/reg_form2.html', {'form': form})  # Ошибки
#     else:
#         form = UserCreationForm()
#     return render(request, 'userRegLog/reg_form2.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "userRegLog/login_form.html", {"form": form})

    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("OK")  # JS проверит отсутствие alert-danger
        else:
            form.add_error(None, "Неверное имя пользователя или пароль")

    return render(request, "userRegLog/login_form.html", {"form": form})


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#             # return HttpResponseRedirect(reverse('profile'))
#
#         # < !-- если пользователь с таким именем/паролем НЕ существует -->
#         return HttpResponseRedirect(reverse('home'))
#
#     else:
#         return HttpResponseRedirect(reverse('home'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
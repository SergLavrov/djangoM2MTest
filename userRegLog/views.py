from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegisterForm
from django.contrib import messages


def home_page(request):
    return render(request, 'userRegLog/home.html')


def reg_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
            # messages.success(request, 'Вы успешно зарегистрированы!')
        else:
            return render(request, 'userRegLog/home.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'userRegLog/home.html', {'form': form})





# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return render(request, 'userRegLog/reg_form.html', {'form': form})
#     else:
#         form = RegisterForm()
#         return render(request, 'userRegLog/reg_form.html', {'form': form})
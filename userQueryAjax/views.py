from django.shortcuts import render
from .forms import RegisterForm
from django.http import JsonResponse

'''
Ajax (Asynchronous JavaScript and XML) — это технология, позволяющая обновлять информацию на странице 
без ее полного перезагрузки. Это особенно важно в современном веб-разработке, где пользователи 
ожидают мгновенных результатов и отзывчивых интерфейсов.
Источник: https://funday24.driverlib.ru/ajax-form-on-error
'''


def home_page(request):
    return render(request, 'userQueryAjax/home2.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        # else:
        #     return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = RegisterForm()
    return render(request, 'userQueryAjax/register_form.html', {'form': form})


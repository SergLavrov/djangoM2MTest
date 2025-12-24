from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home_page, name='home'),
    # path('home/', views.prod_list, name='home'),
    path('register/', views.reg_form, name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

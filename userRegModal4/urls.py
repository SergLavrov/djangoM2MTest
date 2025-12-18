from django.urls import path
from . import views

from django.views.generic import RedirectView

# <!--Через классы представлений !!! -->
urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home_page, name='home'),
    path('reg_success/', views.reg_success, name='reg_success'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_user, name='logout'),           # без класса представления - class LogoutView
]

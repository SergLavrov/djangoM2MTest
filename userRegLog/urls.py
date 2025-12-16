from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home_page, name='home'),
    # path('register/', views.register_view, name='register'),
    path('register/', views.reg_form, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

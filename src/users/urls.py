from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("LoginRegistr/",  views.LoginAndRegisterView.as_view(),
         name='login_registr'),

    path('logout/', LogoutView.as_view(),
         name='logout'),
]
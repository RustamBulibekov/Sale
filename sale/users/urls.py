from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'users'

urlpatterns = [

    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
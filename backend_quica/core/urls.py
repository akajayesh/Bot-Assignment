from django.urls import path
from .views import public_api, protected_api, register_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('public/', public_api),
    path('protected/', protected_api),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register_user)
]

from django.urls import path, include
# from register import views
from django.contrib.auth import views as auth_views
from django.conf import settings
# from django.contrib.auth.views import LogOut
from . import views

urlpatterns = [
    path('list/', views.RegisterListView.as_view(), name='home'),
    path('create/', views.RegisterCreateView.as_view(), name='register-create'),
    path('update/<int:pk>', views.RegisterUpdateView.as_view(), name='register-update'),
    path('login', views.LogInView.as_view(), name="login"),
    path('logout/', views.LogOut.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('facebook/login/', views.login, name='login'),
    path('test/', views.face_login.as_view(), name='facebooklogin'),
]
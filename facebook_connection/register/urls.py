from django.urls import path, include
from register import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/', views.RegisterListView.as_view(), name='home'),
    path('create/', views.RegisterCreateView.as_view(), name='register-create'),
    path('update/<int:pk>', views.RegisterUpdateView.as_view(), name='register-update'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
from django.urls import path

from api.register.views import RegisterCreate , RegisterUpdate , RegisterDelete

urlpatterns = [
    path('create/', RegisterCreate.as_view(), name='register-create-api'),
    path('update/<int:pk>', RegisterUpdate.as_view(), name ='register-update-api'),
    path('delete/<int:pk>', RegisterDelete.as_view(), name ='register-delete-api')
]

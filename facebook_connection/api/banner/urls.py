from django.urls import path

from api.banner.views import Banner_Create, Banner_Update, Banner_Delete, Banner_List

urlpatterns = [
    path('create/', Banner_Create.as_view(), name='banner-create-api'),
    path('list/', Banner_List.as_view(), name ='banner-list-api'),
    path('update/<int:pk>',Banner_Update.as_view(), name ='banner-update-api'),
    path('delete/<int:pk>',Banner_Delete.as_view(), name ='banner-delete-api'),
]
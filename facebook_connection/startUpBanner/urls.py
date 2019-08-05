from django.urls import path
from startUpBanner import views

urlpatterns = [
    path('', views.BannerListView.as_view(), name='banner-list'),
    path('create/', views.BannerCreateView.as_view(), name='banner-create'),
    path('update/<int:pk>', views.BannerUpdateView.as_view(), name='banner-update'),
    path('list/', views.BannerAllListView.as_view(), name ='banner-all-list' ),
    path('singel/<int:pk>', views.BannerDetatilView.as_view(), name ='singel-banner'),
]
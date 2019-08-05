from django.urls import path, include

urlpatterns = [
	path('banner/',include('api.banner.urls')),
	path('register/',include('api.register.urls')),

]
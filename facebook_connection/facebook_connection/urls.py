
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from django.contrib.auth import views as auth_views
# from start_facebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
	# path('', include('start_facebook.urls')),
	path('api/',include('api.urls')),
	path('',include('startUpBanner.urls')),
	path('register/',include('register.urls')),

]
# urlpatterns += i18n_patterns(
# 	path('admin/', admin.site.urls),
# 	# path('', include('start_facebook.urls')),
# 	# path('api/',include('api.urls')),
# 	path('',include('startUpBanner.urls')),
# 	path('register/',include('register.urls')),
# )

if settings.DEBUG:
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import Home

admin.site.site_header = 'Buzz Administration'

urlpatterns = [
    url(r'^api/', include('api.urls')),
    path('', Home.as_view(), name='home'),
    url(r'^accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
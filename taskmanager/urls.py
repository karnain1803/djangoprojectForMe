from django.contrib import admin
from django.template.backends import django
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('web/', include('web.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drf101.api.urls')),
    path('', include('drf101.web.urls')),
]

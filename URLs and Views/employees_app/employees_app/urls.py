from django.contrib import admin
from django.urls import path, include
from employees_app.employees.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('departments/', include('employees_app.employees.urls')),
]

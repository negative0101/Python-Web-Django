from django.urls import path

from employees_app.employees.views import list_departments, department_details, not_found, go_to_home

urlpatterns = (
    path('', list_departments),
    path('<int:id>', department_details),
    path('not-found/',not_found),
    path('go-to-home',go_to_home)
)

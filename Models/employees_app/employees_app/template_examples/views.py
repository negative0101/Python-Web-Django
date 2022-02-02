from django.shortcuts import render


# Create your views here.
from employees_app.employees.models import Employee


def index(request):
    context = {
        'title': 'Employees List',
        'employee': Employee.objects.all(),
    }
    return render(request, 'templates_examples/index.html', context)

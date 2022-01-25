from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
from django.shortcuts import redirect, render


def home(request):
    context = {
        'number': 1234
    }
    return render(request,'index.html',context)


def department_details(request, id):
    if not isinstance(id, int):
        # return 404
        pass
    return HttpResponse(f'This is department {id} {type(id)}')


def list_departments(request):
    return HttpResponse("This are all list departments")


def not_found(request):
    raise Http404()


def go_to_home(request):
    return redirect(to='/')


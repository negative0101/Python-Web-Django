from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# pure python func
# - called with django request object
# - returns request
from djangodemo.web.models import Todo


def index(request):
    context = {
        'title': 'func based view'
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'class based view'
        }

        return render(request, 'index.html', context)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'

        return context


# class RedirectToIndexView(views.RedirectView):
#     url = reverse_lazy('index class-base')


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todos-details.html'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = ('title', 'description', 'category')

from django.shortcuts import render

# Create your views here.
from django.views import generic as views

from testdemos.web.models import Profile


class PetCreateView(views.CreateView):
    model = Profile
    fields= "__all__"
    template_name = 'profile/create.html'

class PetListView(views.ListView):
    model = Profile
    template_name = 'profile/list.html'

class PetDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile/details.html'


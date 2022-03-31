import random

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(15)
from common_tools.web.models import Profile


def show_index(request):
    Profile.objects.create(name='Test Testov',email='test@test.bg')
    profiles = Profile.objects.all()
    paginator = Paginator(profiles, per_page=5)
    if not cache.get('value2'):
        cache.set('value2',random.randint(1,1024),30)

    context = {
        'value': random.randint(1, 1024),
        'value2': cache.get('value2'),
        'profiles_page': paginator.get_page(1)

    }
    return render(request,'index.html',context)



from django.urls import path

from drf101.web.views import IndexView

urlpatterns =[
    path('',IndexView.as_view(),name='index')
]

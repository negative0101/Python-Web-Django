from django.urls import path

from testdemos.web.views import PetCreateView, PetListView, PetDetailsView

urlspatterns = [
    path('create/',PetCreateView.as_view(),name='create profile'),
    path('/',PetListView.as_view(),name='list profile'),
    path('<int:pk>/',PetDetailsView.as_view(),name='details profile'),
]

from django.urls import path

from common_tools.web.views import show_index

urlpatterns = [
    path('', show_index, name='index')
]
import common_tools.web.signals

from django.urls import path

from music_app.main.views import show_index, add_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile

urlpatterns = [
    path('', show_index, name='show_index'),
    path('album/add/', add_album, name='add_album'),
    path('album/details/<int:pk>/', details_album, name='details_album'),
    path('album/edit/<int:pk>/', edit_album, name='edit_album'),
    path('album/delete/<int:pk>/', delete_album, name='delete_album'),

    path('profile/details/', details_profile, name='details_profile'),
    path('profile/delete/', delete_profile, name='delete_profile')
]

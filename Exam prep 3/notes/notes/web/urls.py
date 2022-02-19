from django.urls import path

from notes.web.views import home_page, add_note, edit_note, delete_note, details_note, profile_details, delete_profile, \
    create_profile

urlpatterns = (
    path('', home_page, name='index page'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),


    path('profile/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/create/', create_profile, name='create profile'),

)

from django.urls import path

from todo_app.todo_auth.views import RegisterView, LogoutView, LoginView

urlpatterns =[

    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    # path('logout/',LogoutView.as_view(),name='logout'),
]

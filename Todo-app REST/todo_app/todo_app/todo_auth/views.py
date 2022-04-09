from django.contrib.auth import get_user_model
from rest_framework import generics as api_generic_views
from rest_framework import views as api_views

from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from todo_app.todo_auth.serializers import CreateUserSerializer

UserModel = get_user_model()


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(views.ObtainAuthToken):
    # as long as it inherits views.ObtainAuthToken everything will work
    pass


class LogoutView(api_views.APIView):
    @staticmethod
    def __perform_logout(request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'User logged out'
        })

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)

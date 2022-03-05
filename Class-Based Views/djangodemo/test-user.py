#Wrong
from django.contrib.auth.models import User


# Correct
from django.contrib.auth import get_user_model
UserModel = get_user_model()

UserModel.objects.create_user(
    username='testuser',
    password='12345qwe',
)

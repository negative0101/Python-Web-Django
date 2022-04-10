from django.contrib.auth import get_user_model
from django.db import models
UserModel =get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15, )


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    state = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)

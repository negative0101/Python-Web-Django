from django.db import models


# Create your models here.

class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN)
    image_url = models.URLField()


class Book(models.Model):
    TITLE_MAX_LEN = 30
    TYPE_MAX_LEN = 30

    title = models.CharField(max_length=TITLE_MAX_LEN)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=TYPE_MAX_LEN)



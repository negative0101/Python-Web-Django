import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_username(value):
    if not all(c.isalnum() or c == '_' for c in value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def validate_age(value):
    if value < 0:
        raise ValidationError('Age cannot be less than 0.')


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username,
        ),
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validate_age,
        )
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIPHOP = "Hip Hop Music"
    OTHER = "Other"

    GENRE_CHOICES = (
        POP,
        JAZZ,
        RNB,
        ROCK,
        COUNTRY,
        DANCE,
        HIPHOP,
        OTHER,
    )

    album_name = models.CharField(max_length=ALBUM_NAME_MAX_LEN, unique=True)
    artist = models.CharField(max_length=ARTIST_NAME_MAX_LEN)
    genre = models.CharField(max_length=max(len(g) for g in GENRE_CHOICES),
                             choices=((g, g) for g in GENRE_CHOICES), )
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField()
    price = models.FloatField(validators=(MinValueValidator(0.0),), )

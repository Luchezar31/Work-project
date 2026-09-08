from django.contrib.auth import get_user_model
from django.db import models

from pets.models import Pet
from photos.validators import FileSizeValidator, MinimumLengthValidator

UserModel = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(
        validators=[FileSizeValidator(5)],
        upload_to='uploaded_photos',
    )

    description = models.TextField(
        validators=[MinimumLengthValidator(10)],
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )

    date_of_publication = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True
    )
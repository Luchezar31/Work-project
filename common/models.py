from django.contrib.auth import get_user_model
from django.db import models

from photos.models import Photo

UserModel = get_user_model()

class Comment(models.Model):

    class Meta:
        ordering = ['-date_and_time_of_publication']

    text = models.TextField(
        max_length=300
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    to_photo=models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True
    )

class Like(models.Model):
    to_photo=models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True
    )

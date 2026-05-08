from django import forms

from common.mixins import ReadOnlyMixin
from photos.models import Photo


class PhotoBaseForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ('date_of_publication',)


class PhotoAddForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):

    class Meta:
        model = Photo
        exclude = ('photo','date_of_publication')


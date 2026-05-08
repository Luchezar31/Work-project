from django import forms

from common.mixins import ReadOnlyMixin
from pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('slug',)
        labels = {
            'name':'Pet Name',
            'personal_photo':'Link to Image',
            'date_of_birth': 'Date of birth'

        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                },

            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder':'mm//dd/yyyy'
                }
            ),
            'personal_photo': forms.TextInput(
                attrs={
                    'placeholder': 'Link to image'
                },

            )



        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(ReadOnlyMixin,PetBaseForm):
    pass

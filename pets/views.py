from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.forms import CommentForm
from common.mixins import ProfileOwnerOnlyAccessMixin
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


class AddPetView(LoginRequiredMixin,CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        pet = self.object

        return reverse('profile-details',kwargs={'pk':pet.user.profile.pk})

    def form_valid(self,form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()
        return context

class PetEditView(ProfileOwnerOnlyAccessMixin,UpdateView):
    form_class = PetEditForm
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):

        username = self.request.user.profile.full_name or 'Anonymous'
        pet_slug = self.object.slug


        return reverse('pet-details',kwargs={'username':username, 'pet_slug':pet_slug})

class DeletePetView(DeleteView):
    form_class = PetDeleteForm
    model = Pet
    success_url = reverse_lazy('profile-details',kwargs={'pk':1})
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-delete-page.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['instance'] = self.object

        return kwargs







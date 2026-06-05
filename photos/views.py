from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.forms import CommentForm
from photos.forms import PhotoAddForm, PhotoEditForm
from photos.models import Photo


class PhotoAddView(CreateView):
    form_class = PhotoAddForm
    success_url = reverse_lazy('home')
    template_name = 'photos/photo-add-page.html'

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'


    def get_queryset(self):
        return super().get_queryset().prefetch_related('comment_set','like_set')


    def get_context_data(self,**kwargs):
        context = super().get_context_data()

        context.update({
            'comment_form' : CommentForm(),
        })

        return context



class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse('photo-details',kwargs={'pk':self.object.pk})

class PhotoDeleteView(View):


    def get(self,request,*args,**kwargs):
        photo = Photo.objects.get(pk=kwargs.get('pk'))
        photo.delete()
        return redirect('home')



from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView, FormView
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from common.models import Like
from photos.models import Photo



class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'photos'
    paginate_by = 2
    ordering = 'pk'


    def get_context_data(self,**kwargs):
        kwargs.update({
            'search_form': self.search_form,
            'comment_form':CommentForm()
        })
        return super().get_context_data(**kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()


        self.search_form = SearchForm(self.request.GET or None)

        if  self.search_form.is_valid():

            pet_name = self.search_form.cleaned_data.get('text')
            if pet_name:
                queryset = queryset.prefetch_related('tagged_pets','like_set').filter(
                    tagged_pets__name__icontains=pet_name
                ).distinct()
        return queryset




def like_view(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo.pk}')


def share_view(request,photo_id):

    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details',pk=photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def add_comment_view(request,photo_id):

    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.save()
            return redirect(request.META.get("HTTP_REFERER") + f'#{photo_id}')

    return redirect(request.META.get("HTTP_REFERER") + f'#{photo_id}')


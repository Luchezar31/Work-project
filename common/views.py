from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from common.models import Like
from photos.models import Photo


def common(request):
    all_photos = Photo.objects.prefetch_related('tagged_pets').all()
    search_form = SearchForm(request.GET or None)
    comment_form = CommentForm()

    if search_form.is_valid():
        query = search_form.cleaned_data.get('text')
        all_photos = all_photos.filter(tagged_pets__name__icontains=query)


    context = {
        'photos': all_photos,
        'comment_form':comment_form,
        'search_form':search_form
    }

    return render(request,'common/home-page.html', context)



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


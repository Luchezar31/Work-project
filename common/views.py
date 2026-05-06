from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.models import Like
from photos.models import Photo


def common(request):
    all_photos = Photo.objects.all()

    context = {
        'photos': all_photos
    }

    return render(request,'common/home-page.html', context)



def like_view(request,photo_id):
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



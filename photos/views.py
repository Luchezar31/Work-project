from django.shortcuts import render, redirect

from photos.forms import PhotoAddForm, PhotoEditForm
from photos.models import Photo


# Create your views here.

def photo_add(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects.prefetch_related('comment_set', 'like_set').get(pk=pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.all()

    context = {
        "photo": photo,
        'comments': comments,
        'likes': likes
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):

    photo = Photo.objects.get(pk=pk)

    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('photo-details', pk=pk)

    context = {
        'form':form,
        'photo':photo
    }

    return render(request, 'photos/photo-edit-page.html',context)


def photo_delete(request,pk):

    photo = Photo.objects.get(pk=pk).delete()

    return redirect('home')

from django.shortcuts import render, redirect

from common.forms import CommentForm
from pets.forms import PetCreateForm, PetEditForm
from pets.models import Pet


def pet_add(request):

    form = PetCreateForm(request.POST or None)

    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('profile-details',pk=1)

    context = {
        'form':form
    }


    return render(request,'pets/pet-add-page.html',context)

def pet_details(request,username,pet_slug):
    pet = Pet.objects.prefetch_related('photo_set').get(slug=pet_slug)
    photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet':pet,
        'photos':photos,
        'comment_form':comment_form
    }

    return render(request,'pets/pet-details-page.html',context)

def pet_edit(request,username,pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None,instance=pet)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('pet-details',username=username,pet_slug=pet.slug)

    context = {
        'pet':pet,
        'form':form
    }

    return render(request,'pets/pet-edit-page.html',context)

def pet_delete(request,username,pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(instance=pet)
    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'form':form
    }

    return render(request,'pets/pet-delete-page.html',context)



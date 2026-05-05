from django.shortcuts import render

from pets.models import Pet


def pet_add(request):
    return render(request,'pets/pet-add-page.html')

def pet_details(request,username,pet_slug):
    pet = Pet.objects.prefetch_related('photo_set').get(slug=pet_slug)

    context = {
        'pet':pet
    }

    return render(request,'pets/pet-details-page.html',context)

def pet_edit(request,username,pet_slug):
    return render(request,'pets/pet-edit-page.html')

def pet_delete(request,username,pet_slug):
    return render(request,'pets/pet-delete-page.html')



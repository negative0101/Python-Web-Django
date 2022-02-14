from django.shortcuts import render, redirect

from petstagram.main.forms import CreateProfileForm, EditProfileForm
from petstagram.main.models import Pet, PetPhoto
from petstagram.main.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects \
        .filter(tagged_pets__in=pets) \
        .distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': get_profile,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    profile=get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form':form

    }
    return render(request, 'profile_edit.html',context)


def delete_profile(request):
    return render(request, 'profile_delete.html')

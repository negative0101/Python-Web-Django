from django.shortcuts import render, redirect

from music_app.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from music_app.main.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_index(request):
    profile = get_profile()
    albums = Album.objects.all()
    if not profile:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show_index')
        else:
            form = CreateProfileForm()
        template = 'home-no-profile.html'
        context = {'form': form}
    else:
        template = 'home-with-profile.html'
        context = {'albums': albums,'no_profile':True}
    return render(request, template, context)


def details_profile(request):

    profile = get_profile()
    if profile:
        albums = Album.objects.all()

        albums_len = len(albums)
        context = {
            'albums_len': albums_len,
            'profile': profile
        }
    else:
        return redirect('show_index')
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show_index')
    form = DeleteProfileForm(instance=profile)
    context = {
        'form':form
    }
    return render(request, 'profile-delete.html',context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_index')
    form = CreateAlbumForm()
    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show_index')

    form = EditAlbumForm(instance=album)
    context = {
        'form': form
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show_index')
    form = DeleteAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, 'delete-album.html', context)

from django.shortcuts import render, redirect

# Create your views here.
from notes.web.forms import CreateProfileForm, DeleteProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, \
    DetailsNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()
    if not profile:
        return redirect('create profile')

    context = {
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')

    form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index page')
    else:
        form = DeleteProfileForm(instance=profile)  # check if can remove instance

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    notes = (Note.objects.all())
    num_notes = len([n for n in notes])
    context = {
        'profile': profile,
        'num_notes': num_notes
    }
    return render(request, 'profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')

    form = CreateNoteForm()
    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index page')

    form = EditNoteForm(instance=note)
    context = {
        'form': form
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('index page')
    form = DeleteNoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }

    return render(request, 'note-details.html', context)

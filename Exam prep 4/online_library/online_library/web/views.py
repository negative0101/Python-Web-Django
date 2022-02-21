from django.shortcuts import render, redirect

# Create your views here.
from online_library.web.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm, \
    DeleteBookForm
from online_library.web.models import Profile, Book


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    form = CreateProfileForm()

    context = {
        'no_profile': True,
        'form': form,
        'profile': profile
    }

    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    form = DeleteProfileForm(instance=profile)
    context = {
        'form':form
    }

    return render(request, 'delete-profile.html',context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    form = AddBookForm()
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def details_book(request, pk):
    book_details = Book.objects.get(pk=pk)
    context = {
        'book_details': book_details
    }
    return render(request, 'book-details.html', context)


def edit_book(request, pk):
    book_details = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book_details)
        if form.is_valid():
            form.save()
            return redirect('show index')

    form = EditBookForm(instance=book_details)
    context = {
        'form': form,
        'book_details': book_details
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book_details = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book_details)
        if form.is_valid():
            form.save()
            return redirect('show index')

    form = DeleteBookForm(instance=book_details)
    context = {
        'form': form,
        'book_details': book_details
    }
    return render(request, 'delete-profile.html', context)

from django.shortcuts import render, redirect

from recipes.main.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.main.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = CreateRecipeForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = EditRecipeForm(instance=recipe)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form
    }

    return render(request, 'delete.html', context)


def details_recipe(request,pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe':recipe
    }

    return render(request, 'details.html',context)

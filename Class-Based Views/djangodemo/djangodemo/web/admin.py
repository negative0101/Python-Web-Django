from django.contrib import admin

# Register your models here.
from djangodemo.web.models import Category, Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

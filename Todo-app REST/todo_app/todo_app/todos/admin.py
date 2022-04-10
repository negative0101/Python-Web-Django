from django.contrib import admin

# Register your models here.
from todo_app.todo_auth.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','user__username','is_done')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

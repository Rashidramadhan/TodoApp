from django.contrib import admin
from .models import Todos

class TodosAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed']


admin.site.register(Todos, TodosAdmin)



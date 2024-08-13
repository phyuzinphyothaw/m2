from django.contrib import admin
from .models import CategoryModel,TodoModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(TodoModel)
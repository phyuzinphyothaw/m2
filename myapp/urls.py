from django.urls import path
from .views import category_list,category_create

urlpatterns = [
    path('categories/', category_list, name= 'category_list'),
    path('categories/create/', category_create, name= 'category_create'),
    
]

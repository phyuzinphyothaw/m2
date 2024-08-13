from django.shortcuts import render,redirect
from .models import CategoryModel

from django import forms


def category_list(request):
    categories = CategoryModel.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
# Create your views here.


#from definition
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name', 'image']

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form':form})

from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class TodoModel (models.Model):
    category =models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Create your models here.

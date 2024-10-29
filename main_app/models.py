from django.db import models

from django.urls import reverse

# Create your models here.

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      # Redirecting to cat-detail page after a POST request
      # looking at urls.py 
      return reverse("cat-detail", kwargs={"cat_id": self.id})
  
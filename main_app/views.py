from django.shortcuts import render
from .models import Cat

from django.http import HttpResponse
# Like res.send in node

# Create your views here.

# THIS IS ONLY FOR TODAY FRIDAY (FIRST DAY)
# We are creating a class, and instatiating some objects from
# that class so we can simulate having some data, so we can pass it
# into the cats index
# We are doing this because we don't have a model yet!
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]


def home(request):
  return render(request, 'home.html')

def about(request):
  # render looks inside of the templates
  # folder automatically for your template files!
  return render(request, 'about.html')

def cat_index(request):
  # search psql cats table and get all the rows!
  cats = Cat.objects.all()

# cats/index.html - is looking inside of the 
# templates folder
# we make a folder for each resourse,
# in this case cats
  return render(request, 'cats/index.html', {'cats': cats})

# cat_id comes from the url route! 
# path('cats/<int:cat_id>/', views)
def cat_detail(request, cat_id): # Like req.params
  # find the row in the db that matches the cat_id with
  # the row number
  cat_from_db = Cat.objects.get(id=cat_id)
  # respond with the template
  return render(request, 'cats/detail.html', {'cat': cat_from_db})
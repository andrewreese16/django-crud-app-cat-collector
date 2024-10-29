from django.shortcuts import render, redirect
from .models import Cat

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


from django.http import HttpResponse


# This expects a template in the format of
# templates/<app_name>/<model_name>_form.html
# templates/main_app/cat_form.html
class CatCreate(CreateView):
    model = Cat
    fields = "__all__"


# Go to the models.py file for the Cat model
# to see where the CatCreate redirects to, after
# a POST request


class CatUpdate(UpdateView):
    model = Cat
    # disallow the renaming of a cat by excluding the name field
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"  # refering to a url in the urls.py!


# Like res.send in node


def home(request):
    return render(request, "home.html")


def about(request):
    # render looks inside of the templates
    # folder automatically for your template files!
    return render(request, "about.html")


def cat_index(request):
    # search psql cats table and get all the rows!
    cats = Cat.objects.all()

    # cats/index.html - is looking inside of the
    # templates folder
    # we make a folder for each resourse,
    # in this case cats
    return render(request, "cats/index.html", {"cats": cats})


# cat_id comes from the url route!
# path('cats/<int:cat_id>/', views)
def cat_detail(request, cat_id):  # Like req.params
    # find the row in the db that matches the cat_id with
    # the row number
    cat_from_db = Cat.objects.get(id=cat_id)
    # respond with the template
    feeding_form = FeedingForm()  # creating a form object to pass into!
    return render(
        request, "cats/detail.html", {"cat": cat_from_db, "feeding_form": feeding_form}
    )


def add_feeding(request, cat_id):
    # process the post request and create a feeding!
    form = FeedingForm(request.POST) # Like req.body
    # you're creating a form instance by filling out the form with 
    # the data from the request(form submitting)
    if form.is_valid():
        # don't save it until we add the cat_id
        new_feeding = form.save(commit=False)
        # Makes an in memory representation of out new feeding row in psql 
        new_feeding.cat_id = cat_id
        new_feeding.save() # adds the row to the feeding table
    # redirect to cat-detail page, (cat_id (left) is from the param name)
    
    #import redirect at the top
    return redirect('cat-detail', cat_id=cat_id)
    
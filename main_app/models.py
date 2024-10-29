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


MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        # choices, for a select menu (on a form)
        max_length=1,
        choices=MEALS,
        # default value for the meal will be 'B'
        default=MEALS[0][0],
    )
    # create a cat_id column for our 1 Cat has many Feeding, Feeding belongs to a cat
    # Foriegn Key always goes on the many side
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # if you delete a cat, delete the
    # associated feedings! 

    def __str__(self):
        # get_<field_name>_display() is a magic method
        # to get the human readable value for your choice
        # so 'B' becomes Breakfast when the Feeding is printed!
        return f"{self.get_meal_display()} on {self.date}"

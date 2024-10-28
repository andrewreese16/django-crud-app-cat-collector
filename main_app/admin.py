from django.contrib import admin

# Register your models here.

from .models import Cat

# Full crud access to the cat table in the admin site for our superuser
admin.site.register(Cat)
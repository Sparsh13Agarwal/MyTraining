from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Item

admin.site.register(Item) # whenever we access admin page we can see the item class info.


from django.contrib import admin
from .models import Expenses,Users
 
admin.site.register(Expenses)
admin.site.register(Users)
 #Register the model with the admin
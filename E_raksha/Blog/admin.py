from django.contrib import admin
from .models import *



# Register your models here.

my_models = [Blog , BlogComment]
admin.site.register(my_models)

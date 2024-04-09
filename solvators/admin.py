from django.contrib import admin
from .models import User


# The dot refers to the same directory - in .models
admin.site.register(User)

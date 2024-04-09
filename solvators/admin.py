from django.contrib import admin
from .models import User
from .models import Notes
from .models import Chat


# The dot refers to the same directory - in .models
admin.site.register(User)
admin.site.register(Notes)
admin.site.register(Chat)

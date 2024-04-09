from solvators.sign_up_views import sign_up
from solvators.login_views import login
from django.contrib import admin
from django.urls import path
from solvators import sign_up_views
from solvators import login_views
from solvators import notes_views
from solvators import chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', sign_up_views.sign_up),
    path('login/', login_views.login, name='login'),
    path('complain/', chat_views.chat),
    path('complain/<int:id>',chat_views.chat_detail),
    path('notes/', notes_views.note),


]
from rest_framework import serializers
from .models import User
from .models import Notes
from .models import Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','empid']

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['empid','description','time','location']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['empid','description','time']

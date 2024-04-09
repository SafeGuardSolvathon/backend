from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    empid = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.username

class Notes(models.Model):
    empid = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=False)
    time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.empid

class Chat(models.Model):
    empid = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=False)
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.empid
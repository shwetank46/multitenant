from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

class User(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_user = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
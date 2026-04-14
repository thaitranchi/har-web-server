from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.DecimalField(max_digits=9, decimal_places=2)
    accuracy = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

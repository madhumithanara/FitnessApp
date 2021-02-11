from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_weight = models.IntegerField(default=0)
    current_height = models.IntegerField(default=0)
    ideal_weight = models.IntegerField(default=0)
    ideal_height = models.IntegerField(default=0)
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_weight = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    current_height = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    ideal_weight = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    ideal_height = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    day_date = models.DateTimeField(default=now, editable=True)

class Energy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calorie_intake = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    calorie_burnt = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    heart_rate = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    hours_slept = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    day_date = models.DateTimeField(default=now, editable=True)
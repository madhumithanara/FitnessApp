from django.contrib import admin
from .models import Goal, Energy, Cycle

# Register your models here.
admin.site.register(Goal)
admin.site.register(Energy)
admin.site.register(Cycle)
from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

# unregister the Group 
admin.site.unregister(Group)



# admin registrations
admin.site.register(models.Level)
admin.site.register(models.Exam)
admin.site.register(models.Point)
admin.site.register(models.Leaderboard)
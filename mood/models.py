from django.db import models

# Create your models here.

#creates the DB, rows and columns
class Mood(models.Model):
    streak_date = models.DateField(auto_now = True)
    streak_user = models.CharField(max_length=256)
    streak_mood = models.CharField(max_length=50)

    
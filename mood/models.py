from django.db import models

# Create your models here.

#creates the DB, rows and columns
class Mood(models.Model):
    # streak_date = models.DateField(auto_now = True)
    streak_date = models.DateField()
    streak_user = models.CharField(max_length=256)
    streak_mood = models.CharField(max_length=50)

class Streak(models.Model):
    streak_count = models.IntegerField()
    streak_user = models.CharField(max_length=256)
    last_submit = models.DateField()
    # last_submit = models.DateField(auto_now = True)

    
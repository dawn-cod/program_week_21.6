from django.contrib.auth import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class basicInfo(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    actors = models.CharField(max_length=60)
    episodes = models.PositiveSmallIntegerField(default=0)
    brief_intro = models.TextField()
    # year = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class commentInfo(models.Model):
    id = models.AutoField(primary_key=True)

    plot = models.DecimalField(max_digits=2, decimal_places=0)
    actor_expression = models.DecimalField(max_digits=2, decimal_places=0)
    direction = models.DecimalField(max_digits=2, decimal_places=0)
    screenwriter = models.DecimalField(max_digits=2, decimal_places=0)
    photography = models.DecimalField(max_digits=2, decimal_places=0)
    music = models.DecimalField(max_digits=2, decimal_places=0)
    art = models.DecimalField(max_digits=2, decimal_places=0)
    effects = models.DecimalField(max_digits=2, decimal_places=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    overall = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    basicinfo = models.ForeignKey(basicInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.rating
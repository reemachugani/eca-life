from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Activity(models.Model):
    title = models.CharField(max_length=40)
    eventdate = models.DateField(blank=True)
    venue = models.CharField(max_length=40)
    

    def __unicode__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Activity"



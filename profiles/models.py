import PIL
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class StudentProfile(models.Model):
    user = models.ForeignKey(User, unique=True, editable = False)
    posts = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.first_name + self.user.last_name


from core.settings import TIME_ZONE
from django.db import models
from django.db.models.base import Model

# Create your models here.
class categories(models.Model):
    catname = models.CharField(max_length=30)

class blog(models.Model):
    title= models.CharField(max_length=30,null=True)
    desc = models.CharField(max_length=2000,null=True)
    category = models.CharField(max_length=30,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    photo = models.FileField(upload_to='images/', null=True, verbose_name="")
    username = models.CharField(max_length=30,null=True)
    userid = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.name + ": " + str(self.imagefile)
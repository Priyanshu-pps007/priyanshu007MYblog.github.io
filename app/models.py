from datetime import datetime
from email.policy import default
from django.db import models
from django.forms import ImageField
from numpy import Infinity
from sqlalchemy import null

class diary(models.Model):
    username=models.CharField(max_length=50,default='',null=True)
    text=models.TextField(max_length=50000,default='',null=True)
    photo=models.ImageField(default='',upload_to='images',null=True)
    displaytime=models.CharField(default='',max_length=50000)
    
def __str__(self):
    return self.name


# Create your models here.

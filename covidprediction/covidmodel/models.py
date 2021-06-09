from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class CovidSymptomps(models.Model):
    MY_CHOICES = (('a','Male'),('b','Female'))
    cough = BooleanField(null=False,default=False)
    fever = BooleanField(null=False,default=False)
    sore_throat = BooleanField(null=False, default=False)
    shortness_of_breadth = BooleanField(null=False,default=False)
    head_ache = BooleanField(null= False,default=False)
    gender = models.CharField(max_length=1, choices=MY_CHOICES)
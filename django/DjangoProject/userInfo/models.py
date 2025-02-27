from django.db import models
from designation.models import *

class UserInfo(models.Model):
   name = models.CharField(max_length=35, null=True)
   age = models.IntegerField(default=0) 
   gender = models.CharField(max_length=10, null=True)
   phone = models.CharField(max_length=20, null=True)
   designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)

   def __str__(self):      
       return self.name
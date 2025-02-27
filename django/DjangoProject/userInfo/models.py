from django.db import models


class UserInfo(models.Model):
   name = models.CharField(max_length=35, null=True)
   age = models.IntegerField(default=0) 
   gender = models.CharField(max_length=10, null=True)
   phone = models.CharField(max_length=20, null=True)

   def __str__(self):      
       return self.name
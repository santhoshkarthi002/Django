from django.db import models

class Designation(models.Model):
    designation = models.CharField(max_length=220, null=True)
    
    def __str__(self):      
        return self.designation
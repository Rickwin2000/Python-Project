from django.db import models

class ApiTable(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
   

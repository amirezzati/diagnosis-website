from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name

  
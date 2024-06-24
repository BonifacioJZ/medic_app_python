from django.db import models
from src.class_lib.models import Person
# Create your models here.

class Familiar(Person):
    def __str__(self):
        return f"${self.first_name} ${self.last_name}" 

class Patient(Person):
    familiar = models.ManyToManyField(Familiar,blank=True)
    
    class Meta:
        verbose_name = 'familiar'
        verbose_name_plural = 'familiarws'
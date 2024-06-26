from django.db import models
from src.class_lib.models import Person
# Create your models here.

class Familiar(Person):
    class Meta:
        verbose_name = 'familiar'
        verbose_name_plural = 'familiars'
        
    def __str__(self):
        return f" {self.curp} {self.first_name} {self.last_name}" 

class Patient(Person):
    familiar = models.ManyToManyField(Familiar,blank=True,related_name="familiar")
    
    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
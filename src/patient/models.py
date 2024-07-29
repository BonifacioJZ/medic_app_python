from django.db import models
from django.db.models.signals import pre_save
from src.class_lib.models import Person
from src.allergies.models import Allergies
# Create your models here.

class Familiar(Person):
    class Meta:
        verbose_name = 'familiar'
        verbose_name_plural = 'familiars'
        
    def __str__(self):
        return f" {self.curp} {self.first_name} {self.last_name}" 

class Patient(Person):
    familiar = models.ManyToManyField(Familiar,blank=True,related_name="familiar")
    allergies = models.ManyToManyField(Allergies,blank=True,related_name="allergies")
    
    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
    
    def __str__(self) -> str:
        return f" {self.curp} {self.first_name} {self.last_name}"
    


def patient_pre_save(sender,instance,*args, **kwargs):
    instance.curp.upper()
            
pre_save.connect(patient_pre_save,sender=Patient)

def familiar_pre_save(sender,instance:Familiar,*args, **kwargs):
    instance.curp.upper()

pre_save.connect(familiar_pre_save,sender=Familiar)
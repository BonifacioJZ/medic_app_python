from django.db import models
from src.patient.models import Patient
import uuid
# Create your models here.
class Expedient(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    weight=models.DecimalField(verbose_name="Peso",max_digits=3,decimal_places=0)
    height= models.DecimalField(verbose_name="Altura",max_digits=3,decimal_places=2)
    pulse = models.DecimalField(verbose_name="Pulso",max_digits=3,decimal_places=0)
    temperature = models.DecimalField(verbose_name='Temperatura',max_digits=3,decimal_places=0)
    breathing = models.DecimalField(verbose_name='Respiracion',max_digits=3,decimal_places=0)
    systolic = models.DecimalField(verbose_name='Presion Sistolica',max_digits=3,decimal_places=0)
    diastolic= models.DecimalField(verbose_name='Presion Diastolica',max_digits=3,decimal_places=0)
    patient = models.ForeignKey(Patient,null=False,blank=False,related_name='patient',on_delete=models.CASCADE,verbose_name="Paciente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'expedient'
        verbose_name_plural = 'expedients'
    
    def __str__(self) -> str:
        return f"{self.patient.curp} {self.created_at}"
    
    
    
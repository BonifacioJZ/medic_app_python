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
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'expedient'
        verbose_name_plural = 'expedients'
    
    def __str__(self) -> str:
        return f"{self.patient.curp} {self.created_at}"
    
    def get_imc(self)->float:
        weight = float(self.weight)
        height = float(self.height)
        return weight/pow(height,2)
    
    def get_obesity(self)->str:
        imc = self.get_imc()
        if imc <18.5:
            return "Peso Bajo"
        elif imc < 25:
            return "Normal"
        elif imc < 27:
            return "Sobre Peso 1"
        elif imc < 30:
            return "Sobre Peso 2"
        elif imc < 35:
            return "Obesidad 1"
        elif imc < 40:
            return "Obesidad 2"
        elif imc < 50:
            return "Obesidad Morbida"
        else:
            return "Obesidad Extrema"
    
    def get_blood_pressure(self)->str:
        diastolic = int(self.diastolic)
        systolic = int(self.systolic)
        
        if diastolic<90 and systolic<60:
            return "Hipotension"
        elif diastolic< 120 and systolic<= 80:
            return "Normal"
        elif (diastolic>=120 or diastolic<=129) and (systolic<80):
            return "Elevado"
        elif (diastolic>=130 or diastolic<=139) or (systolic >=80 or systolic<=89):
            return "Hipertension level 1"
        elif (diastolic>=140 or diastolic<=179) or (systolic<=90 or systolic<120):
            return "Hipertension level 2"
        elif (diastolic>=180) or (systolic>=120):
            return "Crisis de Himpertension"
            
        
        
        
            
        
    
    
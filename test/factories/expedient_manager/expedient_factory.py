from src.expedient.models import Expedient
from src.expedient.serializer import ExpedientSerializer

class ExpedientFactory:
    
    def build_expedient_JSON(self,patient):
        return {
            'weight':'120',
            'height':'1.90',
            'pulse':'90',
            'temperature':'35',
            'breathing':'10',
            'systolic':'120',
            'diastolic':'80',
            'patient':patient.id,
        }
    def build_expedient(self,patient):
        expedient = ExpedientSerializer(data=self.build_expedient_JSON(patient))
        expedient.is_valid()
        return expedient.save()
        
    
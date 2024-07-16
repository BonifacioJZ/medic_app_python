from src.patient.models import Patient,Familiar
from src.patient.serializers import PatientSerializer
from faker import Faker
from test.factories.familiar_manager.familiar_factory import FamiliarFactory
faker = Faker()

class PatientFactory:
    
    def build_patient_JSON(self,familiar:Familiar):
        return {
            'first_name':faker.first_name(),
            'last_name':faker.last_name(),
            'curp':'BKVL360219MTLHZA66',
            "birth_day": '1995-03-25',
            'familiar':[
                str(familiar.id),
                ],
        }
    
    def build_patient(self,familiar:Familiar)->Patient:
        patient = self.build_patient_JSON(familiar)
        patient_serializer= PatientSerializer(data=patient)
        patient_serializer.is_valid()
        return patient_serializer.save()
    
        
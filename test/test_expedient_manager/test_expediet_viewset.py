from django.urls import reverse
from rest_framework import status
from test.test_setup import TestSetUp
from test.factories.patient_manager.patient_factory import PatientFactory
from test.factories.familiar_manager.familiar_factory import FamiliarFactory
from test.factories.expedient_manager.expedient_factory import ExpedientFactory

class ExpedientCaseTest(TestSetUp):
    def test_expedient_find(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        expedient = ExpedientFactory().build_expedient(patient)
        
        response = self.client.get(
            reverse('expedient_show',args=[expedient.id]),
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['pulse'],str(expedient.pulse))
        self.assertEqual(str(expedient.diastolic),response.data['diastolic'])
    
    def test_no_found_expedient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        expedient = ExpedientFactory().build_expedient(patient)
        
        response = self.client.get(
            reverse('expedient_show',args=[familiar.id]),
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
    def test_create_expedient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        expedient = ExpedientFactory().build_expedient_JSON(patient)
        
        response =self.client.post(
            reverse('expedient_store'),
            expedient,
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['pulse'],expedient['pulse'])
    
    def test_delete_expedient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        expedient = ExpedientFactory().build_expedient(patient)
        
        response = self.client.delete(
            reverse('expedient_delete',args=[expedient.id]),
            format='json',
        )
        
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
        
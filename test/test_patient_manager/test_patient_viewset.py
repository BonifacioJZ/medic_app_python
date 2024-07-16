import uuid
from faker import Faker
from django.urls import reverse
from rest_framework import status
from test.test_setup import TestSetUp
from test.factories.patient_manager.patient_factory import PatientFactory
from test.factories.familiar_manager.familiar_factory import FamiliarFactory

class PatientTestCase(TestSetUp):
    def test_find_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        response = self.client.get(
            reverse('patient_show',args=[patient.id]),
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['id'],str(patient.id))
    
    def test_not_find_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        response = self.client.get(
            reverse('patient_show',args=[familiar.id]),
            format='json',
        )
        
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(str(patient.id),str(familiar.id))
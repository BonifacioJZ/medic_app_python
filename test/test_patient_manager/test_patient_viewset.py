import uuid
from faker import Faker
from django.urls import reverse
from rest_framework import status
from test.test_setup import TestSetUp
from test.factories.patient_manager.patient_factory import PatientFactory
from test.factories.familiar_manager.familiar_factory import FamiliarFactory

faker = Faker()

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
        
    def test_create_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient_JSON(familiar)
        response = self.client.post(
            reverse('patient_index'),
            patient,
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'],patient['first_name'])
        self.assertEqual(response.data['curp'],patient['curp'])
        
    def test_no_validate_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient_JSON(familiar)
        patient['curp']=''
        patient['first_name']=''
        
        respone = self.client.post(
            reverse('patient_index'),
            patient,
            format='json'
        )
        
        
        self.assertEqual(respone.status_code,status.HTTP_400_BAD_REQUEST,'codigo 404')
        self.assertEqual(respone.data['first_name'][0],'Este campo no puede estar en blanco.')
        self.assertEqual(respone.data['curp'][0],'Este campo no puede estar en blanco.')
        
    def test_update_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        update_patient = PatientFactory().build_patient_JSON(familiar)
        update_patient['first_name'] = faker.first_name()
        update_patient['last_name'] = faker.last_name()
        update_patient['curp'] = 'BKVL360219MTLHZA88'
        
        response = self.client.put(
            reverse('patient_edit',args=[patient.id]),
            update_patient,
            format='json'
        ) 
        
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data['first_name'],patient.first_name)
        self.assertNotEqual(response.data['last_name'],patient.last_name)
        self.assertNotEqual(response.data['curp'],patient.curp)
    
    def test_delete_patient(self):
        familiar = FamiliarFactory().build_familiar()
        patient = PatientFactory().build_patient(familiar)
        
        response = self.client.delete(
            reverse('patient_destroy',args=[patient.id]),
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
        
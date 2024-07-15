import uuid
from faker import Faker
from django.urls import reverse
from rest_framework import status
from test.test_setup import TestSetUp
from test.factories.familiar_manager.familiar_factory import FamiliarFactory

faker = Faker()

class FamiliarTestCase(TestSetUp):
    def test_find_familiar(self):
        familiar = FamiliarFactory().build_familiar()
        response = self.client.get(
            reverse('familiar_show',args=[familiar.id]),
            format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'],familiar.first_name)
        self.assertEqual(response.data['id'],str(familiar.id))
    
    def test_error_to_find_familiar(self):
        FamiliarFactory().build_familiar()
        response = self.client.get(
            reverse('familiar_show',args=[uuid.uuid4()]),
            format = 'json',
        )
        
        self.assertEquals(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_new_familiar(self):
        familiar= FamiliarFactory().build_familiar_JSON()
        response = self.client.post(
            reverse('familiar_index'),
            familiar,
            format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(familiar['first_name'],response.data['first_name'])
        self.assertEqual(familiar['phone'],response.data['phone'])
        self.assertEqual(familiar['email'],response.data['email'])
        
    def test_validation_familiar(self):
        familiar= FamiliarFactory().build_familiar_JSON()
        familiar['first_name'] = ''
        familiar['phone'] = faker.phone_number()
        
        response = self.client.post(
            reverse('familiar_index'),
            familiar,
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['first_name'][0],'Este campo no puede estar en blanco.')
        #self.assertEqual(response.data['phone'][0],'Asegúrese de que este campo no tenga más de 13 caracteres.')
    
    def test_no_pass_unique_validation(self):
        FamiliarFactory().build_familiar()
        familiar = FamiliarFactory().build_familiar_JSON()
        response = self.client.post(
            reverse('familiar_index'),
            familiar,
            format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['curp'][0],'Ya existe familiar con este curp.')
    
    def test_update_familiar(self):
        oldFamiliar=FamiliarFactory().build_familiar()
        familiar = FamiliarFactory().build_familiar_JSON()
        familiar['first_name'] = faker.first_name()
        familiar['last_name']= faker.last_name()
        familiar['email']=faker.email()
        familiar['curp'] = 'BKVL360219MTLHZU67'
        response = self.client.put(
            reverse('familiar_edit',args=[oldFamiliar.id]),
            familiar,
            format='json'
        )  
        print(response.data)  
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data['first_name'],oldFamiliar.first_name)
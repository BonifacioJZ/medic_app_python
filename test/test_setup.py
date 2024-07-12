from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import datetime 

faker = Faker()
class TestSetUp(APITestCase):
    def setUp(self):
        from src.user.models import UserAccount as User
        self.login_url = reverse('jwt-create')
        self.user = User.objects.create_superuser(
            username = 'developer',
            first_name = faker.name(),
            last_name = faker.last_name(),
            password = 'Developer',
            email = faker.email(),
            curp = 'UVUJ720605MTCLAS44',
            birth_day = datetime.datetime.now()
        )
        response = self.client.post(
            self.login_url,
            {
                'username':self.user.username,
                'password': 'Developer'
            },
            follow='json'
        )
        self.assertEqual(status.HTTP_200_OK,response.status_code)
        
        self.token = response.data['access']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ self.token)
        return super().setUp()
         
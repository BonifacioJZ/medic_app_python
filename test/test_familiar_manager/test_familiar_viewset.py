from django.urls import reverse
from rest_framework import status
from test.test_setup import TestSetUp
from test.factories.familiar_manager.familiar_factory import FamiliarFactory

class FamiliarTestCase(TestSetUp):
    def test_find_familiar(self):
        familiar = FamiliarFactory().build_familiar()
        print (familiar)
        response = self.client.get(
            reverse('familiar_show',args=[familiar.id]),
            format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
from src.patient.models import Familiar
from faker import Faker
from datetime import datetime
faker = Faker()

class FamiliarFactory:
    def build_familiar_JSON(self):
        return {
            'first_name': faker.first_name(),
            'last_name':faker.last_name(),
            'address':faker.address(),
            'city':faker.city(),
            'colony':'Av Revolucion',
            'curp':'BKVL360219MTLHZU66',
            'email':faker.email(),
            'phone':'000-000-0000',
            "birth_day": '1997-02-21',
        }
    def build_familiar(self):
        return Familiar.objects.create(**self.build_familiar_JSON())
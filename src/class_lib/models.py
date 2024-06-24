import uuid
import datetime
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True, null=False,blank=False)
    first_name = models.CharField(max_length=255,null=False,blank=False)
    last_name = models.CharField(max_length=255,null=False,blank=False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    colony = models.CharField(max_length=100)
    curp = models.CharField(max_length=18,unique=True,null=False,blank=False)
    birth_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def get_age(self):
        return datetime.now().year - self.birth_day.year
    
    class Meta:
        abstract =True
import uuid
import datetime
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    first_name = models.CharField(max_length=255,null=False,blank=False)
    last_name = models.CharField(max_length=255,null=False,blank=False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    colony = models.CharField(max_length=100)
    curp = models.CharField(max_length=18,unique=True,null=False,blank=False)
    birth_day = models.DateField()
    email = models.EmailField(max_length=255, unique=True, null=False,blank=False)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract =True
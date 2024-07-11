from django.db import models
import uuid

from django.urls import reverse
# Create your models here.

class Allergies(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField()
    

    class Meta:
        verbose_name = "allergie"
        verbose_name_plural = "allergies"

    def __str__(self):
        return self.name



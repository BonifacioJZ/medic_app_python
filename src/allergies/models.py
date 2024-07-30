from django.db import models
import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Allergies(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "allergie"
        verbose_name_plural = "allergies"

    def __str__(self):
        return self.name
    def update_slug(self):
        old_slug = self.slug.split("-")
        self.slug = slugify('{}-{}'.format(
            self.name,old_slug[1]
        ))

def create_slug(sender,instance:Allergies, *args, **kwargs):
    if instance.slug:
        return
    
    id = str(uuid.uuid4())
    instance.slug = slugify('{}-{}'.format(
        instance.name,id[:8]
    ))

pre_save.connect(create_slug,sender=Allergies)

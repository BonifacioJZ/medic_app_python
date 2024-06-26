import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from src.class_lib.models import Person

"""The UserAccountManager class is responsible for creating user accounts and superuser accounts,
    including setting their email, password, and additional fields, and saving them to the database.
    """
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserAccount(AbstractBaseUser,Person, PermissionsMixin):
    username = models.CharField(max_length=150,unique=True,null=False,blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False,blank=False)
    phone = models.CharField(max_length=13,null=False,blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name','email','birth_day','curp']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
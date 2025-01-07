from os import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import  PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django work with our custom user model"""
    def create_user(self, email, password=None):
        """Create and save a new user"""

        if not email:
            raise ValueError('Users must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user=self.create_user(email, password)

        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile" inside our system """
    email = models.EmailField(unique=True)
    name=models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user full name."""
        return self.name

    def get_short_name(self):
        """Used to get a user short name."""
        return self.name

    def __str__(self):
        """Django users this when it needs to convert the object to a string."""
        return self.email
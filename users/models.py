from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.db import models
from django.conf import settings
import uuid
from django.utils import timezone





class UserManager(BaseUserManager):
    """
    A blueprint to create a user instance
    """
    
    def create_user(self, username, email, password, **kwargs):
        """
        A method to create a user instance
        """
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have an email")
        if password is None:
            raise TypeError("Users should have a password")
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    
    def create_superuser(self, username, email, password, **kwargs):
        """
        A method to create a superuser instance
        """
        
        if username is None:
            raise TypeError("Users should have a username")
        
        if email is None:
            raise TypeError("Users should have an email")
        
        if password is None:
            raise TypeError("Users should have a password")
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """
    A blueprint to create a user
    """
    
    id = models.UUIDField(unique=True, primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, db_index=True)
    last_name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
        
    objects = UserManager()    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def get_full_name(self):
        """
        A method to return the full name
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        
        return self.username
    
    
    
    


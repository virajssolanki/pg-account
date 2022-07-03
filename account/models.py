from distutils.command.upload import upload
from sqlite3 import Timestamp
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(verbose_name='full name', max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    
class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = "INCOME"
        EXPENSE = "EXPENSE"

    timestamp = models.DateTimeField(auto_now=False)
    description = models.CharField(verbose_name='description', max_length=256, blank=True, null=True)
    paid_by = models.CharField(max_length=256, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True) 
    type = models.CharField(max_length=256, choices=Type.choices)    

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return str(self.description)

    
  
class ChatFile(models.Model):
    upload_on = models.DateTimeField(auto_now=True)
    chat_file = models.FileField(verbose_name='exported chat', blank=True, null=True)   

    class Meta:
        db_table = 'chat_file'

    def __str__(self):
        return str(self.pk)
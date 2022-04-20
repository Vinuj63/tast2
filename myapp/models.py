# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # # Create your models here.

# class CustomUser(AbstractUser):
# #     # is_student = models.BooleanField(default=False)
# #     # is_teacher = models.BooleanField(default=False)
# #     # mailing_address = models.CharField(max_length=200, blank=True)
#     otp = models.CharField(max_length = 4,blank=False, null=True)
    
#     def __str__(self):
#         return self.email
    
    
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# from django.contrib.auth.base_user import BaseUserManager


from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)
    
    

class CustomUser(AbstractUser):
    username = models.TextField(max_length=10, unique=True, null=True)
    name = models.TextField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length = 4,blank=False, null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
   






from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _ 
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email 
    
#class Profile(models.Model):
 #   first_name = models.CharField(max_length=50)
  #  last_name = models.CharField(max_length=50)
   # bio = models.TextField(max_length=250, null=True, blank=True)
    #age = models.PositiveIntegerField(max_digits=3)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
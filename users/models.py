from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    last_name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    cell_phone = models.CharField (max_length=50, default=' ', null=True, blank=True)


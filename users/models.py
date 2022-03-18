from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
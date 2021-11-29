from django.contrib.auth.models import User
from apps.areas.models import Area
from django.db import models

# Create your models here.
class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.OneToOneField(Area, null=True ,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.get_full_name()


def get_full_name(self):
    return self.get_full_name()

User.add_to_class("__str__", get_full_name)

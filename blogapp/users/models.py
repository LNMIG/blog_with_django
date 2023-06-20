from django.db import models

# Create your models here.
class Rol(models.Model):
    type = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        return self.type

class User(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    avatar = models.CharField(max_length=500, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def created_at(self):
        return self.creation_date
    
    def state(self):
        return self.is_active
    
    def rol_type(self):
      return self.rol

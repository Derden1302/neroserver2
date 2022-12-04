from django.contrib.auth.models import AbstractUser
from django.db import models

class Gusers(models.Model):
    pass
    userid = models.AutoField(primary_key=True)
    password = models.TextField()
    email = models.TextField(blank=True, null=True)
    phone_numper = models.TextField(blank=True, null=True)
    pcon_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gusers'

# Create your models here.
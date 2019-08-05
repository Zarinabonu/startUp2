from django.db import models
from django.contrib.auth.models import User

class StartUpRegister(models.Model):
	username = models.CharField(blank=True, max_length=100)
	password = models.CharField(blank=True, max_length=100)
	contact_num = models.TextField(blank=True)
	contact_email = models.EmailField(max_length=70,blank=True)
# Create your models here.

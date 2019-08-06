from django.db import models
from django.contrib.auth.models import User


class StartUpRegister(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	contact_num = models.TextField(blank=True, null=True)
	contact_email = models.EmailField(blank=True, null=True)
# Create your models here.

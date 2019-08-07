# from django.contrib.auth.models import User
from django.db import models

from register.models import User


class StartUpBanner(models.Model):
	user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	title = models.TextField(blank=True)
	description = models.TextField(blank=True)
	data = models.DateTimeField(auto_now_add=True)


class StartUpField(models.Model):
	user = models.ForeignKey('StartUpBanner',on_delete=models.CASCADE,null=True)
	field = models.FileField(blank=True)

# class StartUpProfil(models.Model):
# 	user = models.ForeignKey(User,=models.CASCADE)










# Create your models here.

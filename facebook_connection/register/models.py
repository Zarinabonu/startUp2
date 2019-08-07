from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import validators
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from rest_framework.authtoken.models import Token


class StartUpRegister(models.Model):
	user = models.OneToOneField('User', on_delete=models.CASCADE)
	contact_num = models.TextField(blank=True, null=True)
	contact_email = models.EmailField(blank=True, null=True)
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(
		('username'),
		max_length=100,
		unique=True,
		help_text=('Required 30 characters or fewer. Letters digits and'
				   '@/./+/-/_only.'),
		validators=[
			validators.RegexValidator(
				r'^[\w.@+-]+$',
				('Enter a valid username.'
				 'This value may contain only letters, numbers '
				 'and @/./+/-/_ charecters.'), 'invalid'),

		],
		error_messages={
			'unique':("A user with that username already exist."),
		})
	email = models.EmailField(('email address'),blank=True, unique=True,null=True, error_messages={
		'unique': ("A user with that email already exists. "),
	})
	last_name = models.CharField(('last name'), max_length=50)

	phone = models.CharField(max_length=64, verbose_name=('user phone'))

	is_staff = models.BooleanField(
		('staff status'),
		default=False,
		help_text=('Designates whether the user can log into this admin '
				   'site.'))
	is_active = models.BooleanField(
		('active'),
		default=True,
		help_text=('Designates whether this user should be treated as '
				   'active. Unselect this instead of deleting accounts.'))

	facebook_id = models.CharField(max_length=200, unique=True, null=True, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	class Meta:
		managed = True
		abstract = False
		db_table = 'auth_user'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	Token.objects.get_or_create(user=instance)

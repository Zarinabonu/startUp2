# Generated by Django 2.2.4 on 2019-08-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20190807_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists. '}, max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]

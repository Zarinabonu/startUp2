# Generated by Django 2.2.4 on 2019-08-05 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190805_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startupregister',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='startupregister',
            name='contact_num',
        ),
    ]

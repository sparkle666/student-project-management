# Generated by Django 4.2 on 2023-11-07 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_projectrequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectRequest',
            new_name='SupervisorRequest',
        ),
    ]

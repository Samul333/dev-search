# Generated by Django 4.0.2 on 2022-03-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_localtion_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='localtion',
            new_name='location',
        ),
    ]
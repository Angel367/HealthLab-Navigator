# Generated by Django 5.0.2 on 2024-04-25 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthLab_Navigator_api', '0016_remove_phone_description_phone_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalinstitution',
            name='main_phone',
        ),
        migrations.RemoveField(
            model_name='medicalinstitutionbranch',
            name='phone',
        ),
    ]

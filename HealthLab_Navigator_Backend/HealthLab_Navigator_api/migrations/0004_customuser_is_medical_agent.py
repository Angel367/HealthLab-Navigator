# Generated by Django 5.0.2 on 2024-04-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthLab_Navigator_api', '0003_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_medical_agent',
            field=models.BooleanField(default=False),
        ),
    ]
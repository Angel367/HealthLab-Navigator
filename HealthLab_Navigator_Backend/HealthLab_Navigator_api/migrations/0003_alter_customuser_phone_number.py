# Generated by Django 5.0.2 on 2024-04-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthLab_Navigator_api', '0002_phone_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер телефона'),
        ),
    ]

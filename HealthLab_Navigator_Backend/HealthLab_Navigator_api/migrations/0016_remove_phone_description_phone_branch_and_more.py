# Generated by Django 5.0.2 on 2024-04-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthLab_Navigator_api', '0015_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='description',
        ),
        migrations.AddField(
            model_name='phone',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Филиал'),
        ),
        migrations.AddField(
            model_name='phone',
            name='institution',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Медицинское учреждение'),
        ),
    ]

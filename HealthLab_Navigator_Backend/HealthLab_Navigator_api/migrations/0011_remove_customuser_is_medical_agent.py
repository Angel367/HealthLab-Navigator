# Generated by Django 5.0.2 on 2024-04-22 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthLab_Navigator_api', '0010_alter_feedback_options_alter_visiting_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_medical_agent',
        ),
    ]

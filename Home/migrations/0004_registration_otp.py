# Generated by Django 4.0.1 on 2023-06-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_registration_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='OTP',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-24 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_remove_chatfaq_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idd', models.CharField(blank=True, max_length=500, null=True)),
                ('Status', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

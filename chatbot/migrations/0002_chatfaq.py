# Generated by Django 4.1.4 on 2023-05-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatFaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=1000, null=True)),
                ('Answer', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

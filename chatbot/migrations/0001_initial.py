# Generated by Django 4.1.4 on 2023-05-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idd', models.CharField(blank=True, max_length=500, null=True)),
                ('qs1', models.CharField(blank=True, max_length=500, null=True)),
                ('qs2', models.CharField(blank=True, max_length=500, null=True)),
                ('qs3', models.CharField(blank=True, max_length=500, null=True)),
                ('qs4', models.CharField(blank=True, max_length=500, null=True)),
                ('qs5', models.CharField(blank=True, max_length=500, null=True)),
                ('ans1', models.CharField(blank=True, max_length=500, null=True)),
                ('ans2', models.CharField(blank=True, max_length=500, null=True)),
                ('ans3', models.CharField(blank=True, max_length=500, null=True)),
                ('ans4', models.CharField(blank=True, max_length=500, null=True)),
                ('ans5', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2023-05-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_chatfaq_idd'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatfaq',
            name='Dictionary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

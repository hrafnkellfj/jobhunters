# Generated by Django 5.0.5 on 2024-05-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_remove_application_city_remove_application_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
    ]

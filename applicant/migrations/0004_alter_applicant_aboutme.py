# Generated by Django 5.0.5 on 2024-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_alter_applicant_aboutme_alter_applicant_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='aboutMe',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 5.0.5 on 2024-05-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0005_applicanteduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
    ]

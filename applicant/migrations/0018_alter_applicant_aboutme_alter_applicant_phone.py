# Generated by Django 5.0.5 on 2024-05-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0017_alter_applicanteducation_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='aboutMe',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
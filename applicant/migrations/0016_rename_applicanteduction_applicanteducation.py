# Generated by Django 5.0.5 on 2024-05-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0015_alter_applicant_aboutme_alter_applicant_city_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplicantEduction',
            new_name='ApplicantEducation',
        ),
    ]

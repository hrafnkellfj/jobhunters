# Generated by Django 5.0.5 on 2024-05-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0008_applicanteduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicanteduction',
            old_name='field_of_study',
            new_name='fieldOfStudy',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-09 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0009_rename_field_of_study_applicanteduction_fieldofstudy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicanteduction',
            old_name='dateEnd',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='applicanteduction',
            old_name='dateStart',
            new_name='start',
        ),
    ]
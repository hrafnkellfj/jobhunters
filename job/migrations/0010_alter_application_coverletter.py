# Generated by Django 5.0.5 on 2024-05-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='coverLetter',
            field=models.CharField(max_length=500),
        ),
    ]

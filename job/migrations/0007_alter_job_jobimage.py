# Generated by Django 5.0.5 on 2024-05-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobImage',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
    ]

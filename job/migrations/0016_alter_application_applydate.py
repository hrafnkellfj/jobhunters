# Generated by Django 5.0.5 on 2024-05-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applyDate',
            field=models.DateField(null=True),
        ),
    ]

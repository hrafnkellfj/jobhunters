# Generated by Django 5.0.5 on 2024-05-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_application_isfinished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(default='Pending', max_length=8),
        ),
    ]
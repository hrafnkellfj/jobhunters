# Generated by Django 5.0.5 on 2024-05-10 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='username',
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

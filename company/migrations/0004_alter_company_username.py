# Generated by Django 5.0.6 on 2024-05-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 5.0.5 on 2024-05-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_remove_company_username_alter_company_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='companyPage',
        ),
    ]

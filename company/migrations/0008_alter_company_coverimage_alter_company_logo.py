# Generated by Django 5.0.5 on 2024-05-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_company_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='coverImage',
            field=models.CharField(blank=True, default='coverImage_missing.png', max_length=999),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(blank=True, default='image_missing.png', max_length=999),
        ),
    ]

# Generated by Django 5.0.5 on 2024-05-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_merge_20240508_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='coverImage',
            field=models.CharField(blank=True, default='coverImage_missing.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(blank=True, default='image_missing.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 5.0.5 on 2024-05-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_alter_recommendation_allowedtocontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='allowedToContact',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

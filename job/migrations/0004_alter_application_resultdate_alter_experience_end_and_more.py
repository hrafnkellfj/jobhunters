# Generated by Django 5.0.5 on 2024-05-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_experiences_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resultDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

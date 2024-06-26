# Generated by Django 5.0.5 on 2024-05-07 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicant', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('jobPercentage', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('postDate', models.DateField()),
                ('dueDate', models.DateField()),
                ('startDate', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverLetter', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=8)),
                ('resultDate', models.DateField(blank=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]

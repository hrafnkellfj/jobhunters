# Generated by Django 5.0.5 on 2024-05-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_company_coverimage_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='coverImage',
            field=models.CharField(blank=True, default='https://img.freepik.com/free-vector/modern-abstract-green-background-with-elegant-elements-vector-illustration_361591-3639.jpg?w=1480&t=st=1715253786~exp=1715254386~hmac=7eef35b858a1aa123ff1c191f92151b030229f9468e78d242e22c77faa75284a', max_length=999),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(blank=True, default='https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg?w=360', max_length=999),
        ),
    ]
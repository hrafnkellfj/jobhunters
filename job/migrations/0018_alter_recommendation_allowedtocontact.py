
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_alter_application_resultdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='allowedToContact',

            field=models.BooleanField(default=False),

            field=models.BooleanField(blank=True, default=False),

        ),
    ]

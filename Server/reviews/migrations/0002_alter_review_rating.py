
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5, message='Rating cannot be greater than 5.'), django.core.validators.MinValueValidator(0, message='Rating cannot be less than 0.')]),
        ),
    ]

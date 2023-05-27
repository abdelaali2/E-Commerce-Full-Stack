# Generated by Django 4.2.1 on 2023-05-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_remove_order_products'),
        ('payments', '0003_payment_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='Orders.order'),
        ),
    ]
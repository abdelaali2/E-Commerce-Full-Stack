# Generated by Django 4.2.1 on 2023-05-22 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_alter_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='product',
        ),
    ]

# Generated by Django 4.0 on 2021-12-31 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_current_price_product_is_on_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_on_sale',
        ),
    ]
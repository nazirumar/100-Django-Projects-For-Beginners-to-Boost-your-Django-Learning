# Generated by Django 5.0.2 on 2024-02-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple_app', '0003_product_available_color_product_available_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]

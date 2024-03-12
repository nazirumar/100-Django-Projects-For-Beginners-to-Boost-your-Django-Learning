# Generated by Django 5.0.2 on 2024-02-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple_app', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('OUT OF STOCK', 'OUT OF STOCK'), ('SALE', 'SALE')], max_length=200, null=True),
        ),
    ]
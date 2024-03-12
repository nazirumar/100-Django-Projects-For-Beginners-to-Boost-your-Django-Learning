# Generated by Django 5.0.2 on 2024-02-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple_app', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='available_size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
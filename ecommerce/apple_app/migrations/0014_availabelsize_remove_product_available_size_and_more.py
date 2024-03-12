# Generated by Django 5.0.2 on 2024-02-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple_app', '0013_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabelSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_size',
        ),
        migrations.AddField(
            model_name='product',
            name='available_size',
            field=models.ManyToManyField(blank=True, null=True, to='apple_app.availabelsize'),
        ),
    ]
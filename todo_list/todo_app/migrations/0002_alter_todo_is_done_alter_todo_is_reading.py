# Generated by Django 5.0.2 on 2024-02-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_done',
            field=models.CharField(blank=True, choices=[('primary', 'primary'), ('read', 'red')], default='red', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_reading',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

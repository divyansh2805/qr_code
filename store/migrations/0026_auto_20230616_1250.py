# Generated by Django 3.1.3 on 2023-06-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20230616_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='services',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
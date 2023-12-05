# Generated by Django 3.1.3 on 2023-12-02 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0072_location_technician_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='store.location'),
        ),
    ]

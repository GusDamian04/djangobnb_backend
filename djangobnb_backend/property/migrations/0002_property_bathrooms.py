# Generated by Django 5.0.2 on 2025-03-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

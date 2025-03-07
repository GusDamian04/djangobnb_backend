# Generated by Django 5.0.2 on 2025-03-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', upload_to='uploads/avatars'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2022-01-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20220117_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeractioningame',
            name='video_end',
            field=models.DecimalField(decimal_places=16, max_digits=32),
        ),
        migrations.AlterField(
            model_name='playeractioningame',
            name='video_start',
            field=models.DecimalField(decimal_places=16, max_digits=32),
        ),
    ]

# Generated by Django 3.0.5 on 2022-01-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0007_auto_20220130_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerposition',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
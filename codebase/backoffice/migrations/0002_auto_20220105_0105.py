# Generated by Django 3.0.5 on 2022-01-05 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playeractioningame',
            name='attributes',
        ),
        migrations.AddField(
            model_name='playeractioningame',
            name='attributes',
            field=models.ManyToManyField(to='backoffice.Attribute'),
        ),
    ]

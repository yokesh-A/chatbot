# Generated by Django 3.0.4 on 2020-08-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_dictionary_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='control',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='usage',
            field=models.IntegerField(default=1),
        ),
    ]
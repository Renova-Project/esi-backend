# Generated by Django 5.0.4 on 2024-06-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0002_diplome'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplome',
            name='is_validated',
            field=models.BooleanField(default=None),
        ),
    ]

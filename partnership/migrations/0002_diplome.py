# Generated by Django 5.0.4 on 2024-06-11 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner/dimplomes/')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnership.partner')),
            ],
        ),
    ]
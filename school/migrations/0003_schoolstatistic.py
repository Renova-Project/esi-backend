# Generated by Django 5.0.4 on 2024-05-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_successstory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-20 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_image_content_type_image_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]

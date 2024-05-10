# Generated by Django 5.0.4 on 2024-05-08 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField()),
                ('event_type', models.TextField()),
                ('event_description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('event_details', models.TextField()),
                ('event_location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examiner_last_name', models.TextField()),
                ('examiner_first_name', models.TextField()),
                ('profession', models.TextField()),
                ('organization', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_description', models.TextField()),
                ('link_image', models.ImageField(upload_to='school/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(upload_to='school/slider/')),
                ('slider_description', models.CharField(max_length=255)),
                ('slider_action_name', models.CharField(max_length=100)),
                ('slider_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_last_name', models.CharField(max_length=50)),
                ('speaker_first_name', models.CharField(max_length=50)),
                ('profession', models.TextField()),
                ('organization', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_theme', models.TextField()),
                ('link_competition', models.URLField(blank=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.event')),
            ],
        ),
        migrations.CreateModel(
            name='Defense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.TextField()),
                ('field', models.TextField()),
                ('defense_date', models.DateTimeField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.event')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_theme', models.TextField()),
                ('conference_date', models.DateTimeField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.event')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('image_description', models.TextField()),
                ('link_image', models.ImageField(upload_to='school/images/')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=50)),
                ('news_type', models.CharField(choices=[('INSIDE', 'something done inside the school'), ('OUTSIDE', 'something done outside the school')], max_length=20)),
                ('news_details', models.TextField()),
                ('news_date', models.DateTimeField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.image')),
            ],
        ),
    ]

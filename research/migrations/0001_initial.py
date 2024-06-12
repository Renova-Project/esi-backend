# Generated by Django 5.0.4 on 2024-06-11 09:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('theme', models.CharField(max_length=255)),
                ('creation_date', models.DateField()),
                ('logo', models.ImageField(upload_to='labs/')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.lab')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_national', models.BooleanField()),
                ('starting_date', models.DateField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.lab')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchteam')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation_date', models.DateField()),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.intern')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchTask',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.intern')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchproject')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchsupervisor')),
            ],
        ),
        migrations.CreateModel(
            name='PermanentMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation_date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchteam')),
            ],
        ),
        migrations.CreateModel(
            name='NonPermanentMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation_date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchteam')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('is_researcher', models.BooleanField(default=False)),
                ('specialty', models.CharField(choices=[('SIT', 'SIT'), ('SIL', 'SIL'), ('SIQ', 'SIQ'), ('SID', 'SID')], max_length=100)),
                ('office', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='teachers/')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='researchteam',
            name='cheif_researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher'),
        ),
        migrations.AddField(
            model_name='researchsupervisor',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher'),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('attachment', models.FileField(upload_to='attachments/')),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='PhDStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thesis_title', models.CharField(max_length=255)),
                ('starting_date', models.DateField()),
                ('defense_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMemberShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('research_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchteam')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='researchteam',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.theme'),
        ),
        migrations.CreateModel(
            name='HasTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.researchproject')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_title', models.CharField(max_length=255)),
                ('training_date', models.DateField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-17 16:10

import autoslug.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('job_type', models.CharField(choices=[('Full Time', 'Fulltime'), ('Part Time', 'Parttime'), ('Internship', 'Internship'), ('Work Visa', 'Workvisa'), ('Remote', 'Remote')], default='Full Time', max_length=30, null=True)),
                ('education', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'Phd'), ('Undergraduate', 'Undergraduate'), ('Any', 'Any')], default='Bachelors', max_length=30, null=True)),
                ('experience', models.CharField(choices=[('Fresher', 'Fresher'), ('1 Year', 'One Year'), ('2 years', 'Two Year'), ('3 Years above', 'Three Year Plus'), ('Any', 'Any')], default='Fresher', max_length=30, null=True)),
                ('industry', models.CharField(choices=[('Information Technology', 'It'), ('Banking', 'Banking'), ('Education', 'Education'), ('Telecommunication', 'Telecommunication'), ('Others', 'Others')], default='Information Technology', max_length=30, null=True)),
                ('salary', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator, django.core.validators.MaxValueValidator(1000000)])),
                ('positions', models.IntegerField(default=1)),
                ('company', models.CharField(max_length=100, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326)),
                ('lastDate', models.DateTimeField(default=job.models.return_date_time)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('skills', models.ManyToManyField(related_name='jobs', to='job.skill')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

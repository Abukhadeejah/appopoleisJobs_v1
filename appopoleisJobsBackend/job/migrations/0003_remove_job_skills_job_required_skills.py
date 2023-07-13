# Generated by Django 4.2.2 on 2023-06-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
        migrations.AddField(
            model_name='job',
            name='required_skills',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
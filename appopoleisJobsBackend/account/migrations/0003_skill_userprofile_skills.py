# Generated by Django 4.2.2 on 2023-06-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userprofile_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(to='account.skill'),
        ),
    ]
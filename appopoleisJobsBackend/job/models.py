from datetime import *
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

import geocoder
import os

from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class JobType(models.TextChoices):
    FullTime = 'Full Time'
    PartTime = 'Part Time'
    Internship = 'Internship'
    WorkVisa = 'Work Visa'
    Remote = 'Remote'


class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    PhD = 'PhD'
    Undergraduate = 'Undergraduate'
    Any = 'Any'


class Experience(models.TextChoices):
    FRESHER = 'Fresher'
    ONE_YEAR = '1 Year'
    TWO_YEAR = '2 years'
    THREE_YEAR_PLUS = '3 Years above'
    Any = 'Any'


class Industry(models.TextChoices):
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Others = 'Others'

def return_date_time():
    now = datetime.now()
    return now + timedelta(days=30)


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField(null=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(
        max_length=30, choices=JobType.choices, default=JobType.FullTime, null=True)
    
    education = models.CharField(
        max_length=30, choices=Education.choices, default=Education.Bachelors, null=True)
    
    experience = models.CharField(
        max_length=30, choices=Experience.choices, default=Experience.FRESHER, null=True)
    
    industry = models.CharField(
        max_length=30, choices=Industry.choices, default=Industry.IT, null=True)
    
    salary = models.IntegerField(
        default=1, validators=[MinValueValidator, MaxValueValidator(1000000)])
    
    positions = models.IntegerField(default=1)

    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))

    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdOn = models.DateTimeField(auto_now_add=True)

    skills = models.ManyToManyField('Skill', related_name='jobs', blank=True)

    slug = AutoSlugField(populate_from='title', unique=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        cords = geocoder.mapquest(self.location, key=os.environ.get('GEOCODER_API'))
        lng = cords.lng
        lat = cords.lat
        self.point = Point(lng, lat)
        super().save(*args, **kwargs)
    

class Skill(models.Model):
    skill = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.skill
    

    
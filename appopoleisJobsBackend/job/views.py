from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.db.models import Avg, Min, Max, Count
from django.utils import timezone


from .serializers import JobSerializer, SkillSerializer, StatsSerializer
from .models import Job, Skill

# Create your views here.
@api_view(['GET'])
def getAllJobs(request):

    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSkills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getJob(request, slug):

    job = get_object_or_404(Job, slug=slug)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def newJob(request):
    data = request.data

    # Extract the skills data from the request data
    skills_data = data.pop('skills', [])

    # Create the job object
    job = Job.objects.create(**data)

    # Associate the skills with the job
    for skill_data in skills_data:
        skill = Skill.objects.get(pk=skill_data['id'])
        job.skills.add(skill)

    # Serialize the job object
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateJob(request, slug):

    job = get_object_or_404(Job, slug=slug)

    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.location = request.data['location']
    job.jobType = request.data['jobType']
    job.industry = request.data['industry']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']
    
    # Update the skills
    skills_data = request.data.get('skills', [])
    job.skills.set(skills_data)

    job.save()

     # Serialize the job object
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteJob(request, slug):
    job = get_object_or_404(Job, slug=slug)
    job.delete()
    return Response({"message": "Job deleted successfully."}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(request, topic):
    args = {'title__icontains': topic}
    jobs = Job.objects.filter(**args)

    if len(jobs) == 0:
        return Response({'message': 'No stats found for {topic}'.format(topic=topic)})

    # Basic statistics
    stats = jobs.aggregate(
        total_jobs=Count('title'),
        avg_positions=Avg('positions'),
        avg_salary=Avg('salary'),
        min_salary=Min('salary'),
        max_salary=Max('salary')
    )

    # Skills in Demand
    skills_in_demand = Skill.objects.filter(jobs__in=jobs).values('skill').annotate(total_jobs=Count('jobs')).order_by('-total_jobs')

    # Calculate percentage for each skill
    total_jobs = stats['total_jobs']
    for skill in skills_in_demand:
        skill['percentage'] = (skill['total_jobs'] / total_jobs) * 100


    response_data = {
        'total_jobs': stats['total_jobs'],
        'avg_positions': stats['avg_positions'],
        'avg_salary': stats['avg_salary'],
        'min_salary': stats['min_salary'],
        'max_salary': stats['max_salary'],
        'skills': skills_in_demand,
    }

    serializer = StatsSerializer(response_data)  # Create a serializer instance
    return Response(serializer.data)

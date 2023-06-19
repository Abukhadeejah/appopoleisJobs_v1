from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import JobSerializer, SkillSerializer
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









    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

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
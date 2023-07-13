from rest_framework import serializers
from .models import Job, Skill, CandidatesApplied

class SkillSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()

    def get_percentage(self, obj):
        if isinstance(obj, dict):
            return obj.get('percentage', 0)
        elif isinstance(obj, Skill):
            return getattr(obj, 'percentage', 0)
        return 0
    
    class Meta:
        model = Skill
        fields = ['id', 'skill', 'percentage']


class StatsSerializer(serializers.Serializer):
    total_jobs = serializers.IntegerField()
    avg_positions = serializers.FloatField()
    avg_salary = serializers.FloatField()
    min_salary = serializers.FloatField()
    max_salary = serializers.FloatField()
    skills = SkillSerializer(many=True)



class JobSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Job
        fields = '__all__'


class CandidateAppliedSerializer(serializers.ModelSerializer):

    job = JobSerializer()

    class Meta:
        model = CandidatesApplied
        fields = ('user', 'resume', 'appliedOn', 'job')
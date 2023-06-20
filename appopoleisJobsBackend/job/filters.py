from django_filters import rest_framework as filters
from .models import Job, Skill


class JobsFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    skills = filters.ModelMultipleChoiceFilter(
        field_name='skills__skill',
        queryset=Skill.objects.all(),
        to_field_name='skill',
    )

    class Meta:
        model = Job
        fields = ('keyword', 'location', 'education', 'job_type', 'experience', 'min_salary', 'max_salary', 'skills')

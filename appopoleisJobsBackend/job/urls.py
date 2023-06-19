from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('skills/', views.getAllSkills, name='skills'),
    path('jobs/<slug:slug>/', views.getJob, name='job')

]
from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.newJob, name='new_Job'),
    path('skills/', views.getAllSkills, name='skills'),
    path('jobs/<slug:slug>/', views.getJob, name='job'),
    path('jobs/<slug:slug>/update/', views.updateJob, name='update_job'),
    path('jobs/<slug:slug>/delete/', views.deleteJob, name='delete_job'),
    path('stats/<slug:topic>/', views.getTopicStats, name='get_topic_stats'),

]
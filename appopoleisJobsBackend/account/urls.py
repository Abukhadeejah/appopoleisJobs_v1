from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('me/', views.currentUser, name='current_user'),
    path('me/updateuser/', views.updateUser, name='update_user'),
    path('upload/resume/', views.uploadResume, name='upload_resume')
]
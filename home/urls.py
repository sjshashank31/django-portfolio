from django.urls import path, re_path

from . import views


app_name = 'home'

urlpatterns = [
    path('', views.home),
    path('already_user/', views.get_user, name='already-user'),
    path('createportfolio/<slug>', views.index, name='create'),
    path('info/', views.create_info, name='info'),
    path('detail/<slug>/', views.detail_view, name='detail'),
    path('<slug>/update_info/', views.update_info, name='update-info'),
    path('skill/<slug>/', views.skill_info, name='skill'),
    path('update_skill/<slug>/<str:skill>/', views.update_skill, name='update-skill'),
    path('delete_skill/<slug>/<str:skill>/', views.delete_skill, name='delete-skill'),
    path('skill_detail/<slug>/', views.skill_detail_view, name='skill-details'),
    path('education/<slug>/', views.education_info, name='education'),
    path('education_detail/<slug>/', views.education_detail_view, name='education-details'),
    path('update_education/<slug>/<str:course>/', views.update_education, name='update-education'),
    path('delete_education/<slug>/<str:course>/', views.delete_education, name='delete-education'),
    path('service/<slug>/', views.service_info, name='service'),
    path('service_detail/<slug>/', views.service_detail_view, name='service-details'),
    path('update_service/<slug>/<str:service_name>/', views.update_service, name='update-service'),
    path('delete_service/<slug>/<str:service_name>/', views.delete_service, name='delete-service'),
    path('work/<slug>/', views.work_info, name='work'),
    path('work_detail/<slug>/', views.work_detail_view, name='work-details'),
    path('update_work/<slug>/<str:project_name>/', views.update_work, name='update-work'),
    path('delete_work/<slug>/<str:project_name>/', views.delete_work, name='delete-work'),
    path('experience/<slug>/', views.experience_info, name='experience'),
    path('experience_detail/<slug>/', views.experience_detail_view, name='experience-details'),
    path('update_experience/<slug>/<organisation_name>/', views.update_experience, name='update-experience'),
    path('delete_experience/<slug>/<organisation_name>/', views.delete_experience, name='delete-experience'),
    path('create_cv/<slug>', views.create_cv, name='create-cv'),

]
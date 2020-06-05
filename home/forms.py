from django import forms
from .models import UserInfo, Skill, Study, Service, Work, Experience


class InfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'mobile_no', 'email', 'about', 'profession', 'place', 'profile_picture']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'percent']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['board_or_univ', 'course', 'school_or_college', 'cgpa_or_percent', 'cgpa']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'description']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['organisation_name', 'post', 'joining_date', 'ending_date', 'work_experience']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['project_name', 'project_type', 'project_link', 'project_image']


class GetUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['slug']

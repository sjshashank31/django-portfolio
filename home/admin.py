from django.contrib import admin
from .models import UserInfo, Study, Skill, Service, Work, Experience

admin.site.register(UserInfo)
admin.site.register(Study)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Work)
admin.site.register(Experience)

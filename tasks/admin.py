from django.contrib import admin
from tasks.models import Task, Tag, Picture, Organization

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Picture)
admin.site.register(Organization)

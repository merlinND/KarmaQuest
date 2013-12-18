from django.contrib import admin
from tasks.models import UserInformation, Task, Tag, Picture

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Picture)
admin.site.register(UserInformation)

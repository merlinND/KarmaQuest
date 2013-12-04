from django.contrib import admin
from tasks.models import User, Task, Tag, Picture

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Picture)

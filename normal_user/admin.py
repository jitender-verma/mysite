from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserType)
admin.site.register(InvalidAttempts)
admin.site.register(UserDetails)
admin.site.register(ManagerTimezones)
admin.site.register(StaffStatusModel)
admin.site.register(CommentsModel)
admin.site.register(AlertModel)
admin.site.register(SavedDocumentModel)
admin.site.register(Departments)
admin.site.register(AssignedDepartments)
admin.site.register(Cities)
admin.site.register(TaskModel)
admin.site.register(ManagerDetails)
admin.site.register(OnlineStatusModel)
admin.site.register(EmailModel)
admin.site.register(ScheduleTiming)
admin.site.register(Functions)
admin.site.register(ChatMessage)
admin.site.register(ChatThread)
admin.site.register(Tasks)
admin.site.register(ScheduleTime)
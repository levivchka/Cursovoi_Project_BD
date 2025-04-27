from django.contrib import admin

# Register your models here.

from .models import Task

admin.site.register(Task)



from .models import Shedule

admin.site.register(Shedule)

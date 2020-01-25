from django.contrib import admin

# Register your models here.
from houseapp.models import House, Task

admin.site.register(House)
admin.site.register(Task)
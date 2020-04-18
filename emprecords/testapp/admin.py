from django.contrib import admin
from testapp.models import employee

# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    list_display=['id','empno','empname','empsal','empaddr']

admin.site.register(employee,employeeAdmin)

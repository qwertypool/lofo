from django.contrib import admin
from testapp.models import Employee,Company
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['enum','ename','esal','eaddr']

class CompanyAdmin(admin.ModelAdmin):
    list_display=['cnum','cname','clocation']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company,CompanyAdmin)
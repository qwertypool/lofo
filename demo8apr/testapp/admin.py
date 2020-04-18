from django.contrib import admin
from testapp.models import Myself,Enemies,Demo
# Register your models here.
class MyselfAdmin(admin.ModelAdmin):
    list_display=['name','age','proffession']

class EnemiesAdmin(admin.ModelAdmin):
    list_display = ['name','age','proffession']

class DemoAdmin(admin.ModelAdmin):
    list_display=['subject','marks']

admin.site.register(Enemies, EnemiesAdmin)
admin.site.register(Myself,MyselfAdmin)
admin.site.register(Demo,DemoAdmin)
from django.contrib import admin

# Register your models here.
class adharAdmin(admin.ModelAdmin):
    list_display=['name','uid']

admin.site.register(adhar,adharAdmin)
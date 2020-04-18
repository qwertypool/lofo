from django.contrib import admin
from testapp.models import Lost,Found
# Register your models here.

class LostAdmin(admin.ModelAdmin):
    list_display = ('name','uid','card')

class FoundAdmin(admin.ModelAdmin):
    list_display = ('name','uid','card')

admin.site.register(Lost, LostAdmin)
admin.site.register(Found, FoundAdmin)


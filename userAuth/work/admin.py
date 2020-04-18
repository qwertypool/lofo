from django.contrib import admin
from work.models import Lost,Found

# Register your models here.
class LostAdmin(admin.ModelAdmin):
    list_display = ('name','uid','card','details')

class FoundAdmin(admin.ModelAdmin):
    list_display = ('name','uid','card','cardholder_name','details')

admin.site.register(Lost, LostAdmin)
admin.site.register(Found, FoundAdmin)
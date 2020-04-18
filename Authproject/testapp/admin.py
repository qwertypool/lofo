from django.contrib import admin
from testapp.models import Adhar,VoterId,Passport,Pan,Atm,Fadhar
# Register your models here.
class AdharAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

class VoterAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

class PassportAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

class PanAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

class AtmAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

class FadharAdmin(admin.ModelAdmin):
    list_display=['id','name','uid']

admin.site.register(Adhar,AdharAdmin)
admin.site.register(VoterId,VoterAdmin)
admin.site.register(Passport,PassportAdmin)
admin.site.register(Pan,PanAdmin)
admin.site.register(Atm,AtmAdmin)
admin.site.register(Fadhar,FadharAdmin)
from django.contrib import admin
from .models import *

class ResumeAdmin(admin.ModelAdmin):
    list_display=[]
class EducationAdmin(admin.ModelAdmin):
    list_display=[]
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','mail','phone','feedback']

admin.site. register(Contact, ContactAdmin)

class LoginDataAdmin(admin.ModelAdmin):
    list_display = ['email','password']

admin.site.register(LoginData, LoginDataAdmin) 

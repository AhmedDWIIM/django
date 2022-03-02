from django.contrib import admin

from .models import Question,Member

class QuestionAdmin(admin.ModelAdmin):
    fields =['text']

class MemberAdmin(admin.ModelAdmin):
    fields =['text']
    fields =['text']
    fields =[0]
    
admin.site.register(Member)
# Register your models here.

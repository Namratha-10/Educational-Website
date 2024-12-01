from django.contrib import admin
from app1.models import registration

# Register your models here.
class registrationAdmin(admin.ModelAdmin):
    list_display=[ 'student_name','parent_name','phone','email']
admin.site.register(registration,registrationAdmin)

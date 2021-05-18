from django.contrib import admin
from myApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l=['id','ename','eage','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)
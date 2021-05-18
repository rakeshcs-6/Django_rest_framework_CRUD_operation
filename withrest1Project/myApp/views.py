from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse
import io 
import json
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from myApp.models import Employee
from myApp.serializers import Employeeserializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class Employee_CRUD_cbv(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id = id)
            eserializers = Employeeserializer(emp)
            json_data = JSONRenderer().render(eserializers.data)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            qs = Employee.objects.all()
            eserializers = Employeeserializer(qs,many = True)
            json_data = JSONRenderer().render(eserializers.data)
            return HttpResponse(json_data,content_type = 'application/json')
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        eserializers = Employeeserializer(data = pdata)
        if eserializers.is_valid():
            eserializers.save()
            msg = {'msg':'created succesfull'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type = 'application/json')
        msg = {'msg':'created unsuccesfull'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def put(self,request,*args,**kwrags):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id = id)
        eserializers = Employeeserializer(emp,data = pdata)
        if eserializers.is_valid():
            eserializers.save()
            msg = {'msg':'updated succesfull'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            json_data = JSONRenderer().render(eserializers.errors)
            return HttpResponse(json_data,content_type = 'application/json',status = 400)

    
    def delete(self,request,*args,**kwrags):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id = id)
        emp.delete()
        msg = {'msg':'deletion succesfull'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type = 'application/json')





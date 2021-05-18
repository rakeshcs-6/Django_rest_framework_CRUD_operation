from rest_framework import serializers
from myApp.models import Employee

class Employeeserializer(serializers.Serializer):
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.ename = validated_data.get('ename',instance.ename)
        instance.eage = validated_data.get('eage',instance.eage)
        instance.esal = validated_data.get('esal',instance.esal)
        instance.eaddr = validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance

    ename = serializers.CharField(max_length = 30)
    eage = serializers.IntegerField()
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length =50)
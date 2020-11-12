from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . serializers import employeeSerializer
from . models import employees

class employeeList(APIView):
    def get(self,request):
        employee=employees.objects.all()
        serializer=employeeSerializer(employee,many=True)
        return Response(serializer.data)
from django.shortcuts import render
from rest_framework import viewsets
from planapi.models import Company,GetPlans
from planapi.serializers import CompanySerializer,Getplansserializers
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class GetplansViewSet(viewsets.ModelViewSet):
    queryset = GetPlans.objects.all()
    serializer_class = Getplansserializers
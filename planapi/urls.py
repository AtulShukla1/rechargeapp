from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from planapi.views import CompanyViewSet,GetplansViewSet


router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'plans',GetplansViewSet)



urlpatterns = [
    path('',include(router.urls))
]

from django.contrib import admin
from django.urls import path,include
from .views import home_page,blank


urlpatterns = [
    path('',blank),
    path('admin/', admin.site.urls),
    path("home/", home_page),
    path("planapi/v1/",include('planapi.urls'))
]

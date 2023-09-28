"""
URL configuration for corporate_assets_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import *

urlpatterns = [
    path("", home, name="home"),
    path("update_company/<id>/", update_company, name="update_company"),
    path("delete_company/<id>/", delete_company, name="delete_company"),
    path("company_info/<id>/", company_info, name="company_info"),
    path("company_info/<id>/employee/", employee_all, name="employee_all"),
    path("company_info/<comp_id>/update_employee/<employ_id>/", update_employee, name="update_employee"),
    path("company_info/<comp_id>/delete_employee/<employ_id>/", delete_employee, name="delete_employee"),
    path("company_info/<comp_id>/employee/<employ_id>/", employee_info, name="employee_info"),
    path("company_info/<comp_id>/employee/<employ_id>/assign/", employ_rent, name="employ_rent"),
    path("company_info/<id>/equipment/", equipment_all, name="equipment_all"),
    path("company_info/<comp_id>/update_equipment/<equip_id>/", update_equipment, name="update_equipment"),
    path("company_info/<comp_id>/delete_equipment/<equip_id>/", delete_equipment, name="delete_equipment"),
    path("company_info/<comp_id>/equipment/<equip_id>/assign/", equip_assign, name="equip_assign"),
    path("admin/", admin.site.urls),
]

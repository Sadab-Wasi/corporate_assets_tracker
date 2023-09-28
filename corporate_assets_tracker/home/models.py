from django.db import models


# Company model structure
class Companies(models.Model):
    name = models.CharField(unique=True, max_length=100)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Employee model structure
class Employees(models.Model):
    name = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_id = models.ForeignKey(Companies, blank=True, default=None, related_name=("employ_comp_id"), on_delete=models.CASCADE)


# Equipment model structure
class Equipments(models.Model):
    name = models.CharField(unique=True, max_length=100)
    condition = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_id = models.ForeignKey(Companies, blank=True, default=None, related_name=("equip_comp_id"), on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employees, blank=True, default=None, null=True, related_name=("equip_employ_id"), on_delete=models.CASCADE)

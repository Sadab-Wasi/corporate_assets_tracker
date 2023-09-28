from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Companies, Employees, Equipments


# home views
def home(request):
    companies = []

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        location = data.get("location")

        Companies.objects.create(name=name, location=location)

        return redirect("/")
    else:
        querySet = Companies.objects.all()
        companies = querySet

    return render(request, "index.html", context={"page": "Home", "companies": companies})


def update_company(request, id):
    querySet = Companies.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        location = data.get("location")

        querySet.name = name
        querySet.location = location

        querySet.save()

        return redirect("/")

    return render(request, "update_company.html", context={"page": "update_company", "company": querySet})


def delete_company(request, id):
    querySet = Companies.objects.get(id=id)
    querySet.delete()

    return redirect("/")


def company_info(request, id):
    querySet = Companies.objects.get(id=id)

    return render(request, "company_info.html", context={"page": "Company Info", "company": querySet})


def employee_all(request, id):
    company = Companies.objects.get(id=id)
    employees = []

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        email = data.get("email")
        company_id = company

        Employees.objects.create(name=name, email=email, company_id=company_id)

        return redirect("/company_info/" + id + "/employee/")
    else:
        querySet = Employees.objects.filter(company_id__id=id)
        employees = querySet

    return render(
        request, "employee.html", context={"page": "Company Info", "company": company, "employees": employees}
    )


def update_employee(request, comp_id, employ_id):
    company = Companies.objects.get(id=comp_id)
    querySet = Employees.objects.get(id=employ_id)

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        email = data.get("email")

        querySet.name = name
        querySet.email = email

        querySet.save()

        return redirect("/company_info/" + comp_id + "/employee/")

    return render(
        request, "update_employee.html", context={"page": "Update employee", "company": company, "employee": querySet}
    )


def delete_employee(request, comp_id, employ_id):
    querySet = Employees.objects.get(id=employ_id)
    querySet.delete()

    return redirect("/company_info/" + comp_id + "/employee/")


def employee_info(request, comp_id, employ_id):
    company = Companies.objects.get(id=comp_id)
    employee = Employees.objects.get(id=employ_id)

    if request.method == "POST":
        data = request.POST

        equip_id = data.get("equip_id")
        condition = data.get("condition")

        querySet = Equipments.objects.get(id=equip_id)

        querySet.employee_id = None
        querySet.condition = condition
        
        querySet.save()

        return redirect("/company_info/" + comp_id + "/employee/" + employ_id)
    else:

        criterion1 = Q(company_id__id=comp_id)
        criterion2 = Q(employee_id__id=employ_id)
        querySet = Equipments.objects.filter(criterion1 & criterion2)

    return render(request, "employee_info.html", context={"page": "Company Info", "company": company, "employee": employee, "equipments": querySet})


def employ_rent(request, comp_id, employ_id):
    company = Companies.objects.get(id=comp_id)
    employee = Employees.objects.get(id=employ_id)
    querySet = []

    if request.method == "POST":
        data = request.POST

        equip_id = data.get("equipment_id")
        querySet = Equipments.objects.get(id=equip_id)

        querySet.employee_id = employee
        
        querySet.save()

        return redirect("/company_info/" + comp_id + "/employee/" + employ_id)
    else:

        criterion1 = Q(company_id__id=comp_id)
        criterion2 = Q(employee_id=None)
        querySet = Equipments.objects.filter(criterion1 & criterion2)

    return render(request, "employee_rent.html", context={"page": "Company Info", "company": company, "employee": employee, "equipments": querySet})



def equipment_all(request, id):
    company = Companies.objects.get(id=id)
    equipments = []

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        condition = data.get("condition")
        company_id = company
        employee_id = None

        Equipments.objects.create(name=name, condition=condition, company_id=company_id, employee_id=employee_id)

        return redirect("/company_info/" + id + "/equipment/")
    else:
        querySet = Equipments.objects.filter(company_id__id=id)
        equipments = querySet

    return render(
        request, "equipments.html", context={"page": "Company Info", "company": company, "equipments": equipments}
    )


def update_equipment(request, comp_id, equip_id):
    company = Companies.objects.get(id=comp_id)
    querySet = Equipments.objects.get(id=equip_id)

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        condition = data.get("condition")

        querySet.name = name
        querySet.condition = condition

        querySet.save()

        return redirect("/company_info/" + comp_id + "/equipment/")

    return render(
        request, "update_equipment.html", context={"page": "Update Equipment", "company": company, "equipment": querySet}
    )


def delete_equipment(request, comp_id, equip_id):
    querySet = Equipments.objects.get(id=equip_id)
    querySet.delete()

    return redirect("/company_info/" + comp_id + "/equipment/")


def equip_assign(request, comp_id, equip_id):
    company = Companies.objects.get(id=comp_id)
    equipment = Equipments.objects.get(id=equip_id)
    querySet = []

    if request.method == "POST":
        data = request.POST
        print(data)

        employ_id = data.get("employee_id")
        querySet = Employees.objects.get(id=employ_id)

        equipment.employee_id = querySet
        
        equipment.save()

        return redirect("/company_info/" + comp_id + "/equipment")
    else:

        querySet = Employees.objects.filter(company_id__id=comp_id)

    return render(request, "equipment_assign.html", context={"page": "Company Info", "company": company, "employees": querySet, "equipment": equipment})


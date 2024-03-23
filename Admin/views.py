from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")

def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':dis})
    else:
        return render(request,"Admin/District.html",{'data':dis})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"Admin\District.html",{"editdata":editdata})


def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,"Admin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"Admin\Place.html",{"editdata":editdata,"districtdata":district})


def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return render(request,"Admin/AdminRegistration.html",{'data':data})
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editdata":editdata})


def employeeInsertSelect(request):
    data=tbl_employee.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        gender=request.POST.get('gender')
        dept=request.POST.get('ddlDept')
        salary=request.POST.get('txtsalary')
        tbl_employee.objects.create(emp_name=name,emp_gender=gender,emp_dept=dept,emp_salary=salary)
        return render(request,"Admin/EmployeeDetails.html",{'data':data})
    else:
        return render(request,"Admin/EmployeeDetails.html",{'data':data})

def delEmployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect("WebAdmin:employeeInsertSelect")


def employeeRegUpdate(request,eid):
    editdata=tbl_employee.objects.get(id=eid)
    if request.method=="POST":
        editdata.emp_name=request.POST.get("txtname")
        editdata.emp_gender=request.POST.get("gender")
        editdata.emp_dept=request.POST.get("ddlDept")
        editdata.emp_salary=request.POST.get("txtsalary")
        editdata.save()
        return redirect("WebAdmin:employeeInsertSelect")
    else:
        return render(request,"Admin\EmployeeDetails.html",{"editdata":editdata})

def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})
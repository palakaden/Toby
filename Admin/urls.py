from django.contrib import admin
from django.urls import path
from Admin import views

app_name="WebAdmin"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),


    path('EmployeeDetails/', views.employeeInsertSelect,name="employeeInsertSelect"),
    path('delEmployee/<int:did>', views.delEmployee,name="delEmployee"),
    path('employeeRegUpdate/<int:eid>',views.employeeRegUpdate,name="employeeRegUpdate"),


    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),
    

]
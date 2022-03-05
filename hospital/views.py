# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,redirect
#from .models import Picto,userlike,Profile
from .forms import DoctorForm,DepartmentForm,PatientForm,WorksforForm,NurseForm,AdmittedForm,EmergencyForm

from django.contrib.auth.decorators import login_required
from django.db import connection
# Create your views here.




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def home(request):
    #title="welcome %s"%request.user
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    #print >>sys.stderr,(dept_dict)
    cursor.close()
    return render(request,'index.html',{'departments':dept_dict})

@login_required
def adddept(request):
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        cursor = connection.cursor()
        if dept_form.is_valid():
                    #print >>sys.stderr, type(int(request.POST['department_num']))
                    dept_num = dept_form.cleaned_data['department_num']
                    #print >>sys.stderr,type(dept_num)
                    department_name = dept_form.cleaned_data['department_name']
                    description = dept_form.cleaned_data['description']
                    floor=dept_form.cleaned_data['floor']
                    
                    add_dept = ("INSERT INTO department  VALUES (%s, %s, %s, %s,%s,%s)")
                    data_dept = (dept_num,department_name,description,"0","0",floor)
                    print(data_dept)
                    cursor.execute(add_dept, data_dept)
                    cursor.close()
                    return redirect('home')
    else:
        dept_form = DepartmentForm()
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    cursor.close() 
    return render(request,'addepartment.html',{'dept_form': dept_form,'departments':dept_dict})

@login_required
def addnurse(request):
    if request.method == 'POST':
        nurse_form = NurseForm(request.POST)
        cursor = connection.cursor()
        if nurse_form.is_valid():
                    #print >>sys.stderr, type(int(request.POST['nurse_id']))
                    nurse_id = nurse_form.cleaned_data['nurse_id']
                    #print >>sys.stderr,type(nurse_id)
                    name = nurse_form.cleaned_data['name']
                    address=nurse_form.cleaned_data['address']
                    department_num=nurse_form.cleaned_data['department']
                    add_nurse = ("INSERT INTO nurses  VALUES (%s, %s, %s, %s)")
                    data_nurse = (nurse_id,name,address,department_num.department_num)
                    cursor.execute(add_nurse, data_nurse)
                    
                    department_num=str(department_num.department_num)
                    cursor.execute("Select total_worker_count from department  where department_num=%s",department_num)
                    dept_det=dictfetchall(cursor)
                    #print >>sys.stderr,dept_det[0]["total_worker_count"]
                    t_count=dept_det[0]["total_worker_count"]+1
                    t_count =str(t_count)
                    cursor.execute("update department set total_worker_count=%s where department_num=%s",(t_count,department_num))
                                        
                    cursor.close()
                    return redirect('home')
    else:
        nurse_form = NurseForm() 
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)
    cursor.close() 
    return render(request,'addnurse.html',{'nurse_form': nurse_form,'departments':dept_dict})

@login_required
def addemergency(request):
    if request.method == 'POST':
        emergency_form = EmergencyForm(request.POST)
        cursor = connection.cursor()
        if emergency_form.is_valid():
                    #print >>sys.stderr, type(int(request.POST['nurse_id']))
                    date = emergency_form.cleaned_data['date']
                    #print >>sys.stderr,type(nurse_id)
                    doctor = emergency_form.cleaned_data['doctor']
                    nurse = emergency_form.cleaned_data['nurse']
                    add_emergency = ("INSERT INTO emergency  VALUES (%s, %s, %s)")
                    data_emergency = (date,doctor.employee_id,nurse.nurse_id)
                    cursor.execute(add_emergency, data_emergency)
                    cursor.close()
                    return redirect('home')
    else:
        emergency_form = EmergencyForm()
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)
    cursor.close() 
    return render(request,'addemergency.html',{'emergency_form': emergency_form,'departments':dept_dict})

@login_required
def addpatient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        admitted_form = AdmittedForm(request.POST)
        cursor = connection.cursor()
        if patient_form.is_valid()  and  admitted_form.is_valid():
                    #print >>sys.stderr, type(int(request.POST['department_num']))
                    patient_id = patient_form.cleaned_data['patient_id']
                    #print >>sys.stderr,type(dept_num)
                    patient_name = patient_form.cleaned_data['patient_name']
                    dt_birth = patient_form.cleaned_data['dt_birth']
                    patient_address = patient_form.cleaned_data['patient_address']
                    add_patient = ("INSERT INTO patient  VALUES (%s, %s, %s, %s)")
                    data_patient = (patient_id,patient_name,dt_birth,patient_address)
                    cursor.execute(add_patient, data_patient)
                    patient_id = patient_form.cleaned_data['patient_id']
                    department_num = admitted_form.cleaned_data['department']
                    date_admission = admitted_form.cleaned_data['date_admission']
                    date_discharge = admitted_form.cleaned_data['date_discharge']
                    doctor = admitted_form.cleaned_data['doctor']
                    prescription = admitted_form.cleaned_data['prescription']
                    add_admission = ("INSERT INTO admitted(patient_id,department_num , date_admission , date_discharge  ,doctor_id, prescription )  VALUES (%s,%s,%s, %s, %s,  %s)")
                    data_admission = (patient_id,department_num.department_num, date_admission , date_discharge ,doctor.employee_id  , prescription )
                    cursor.execute(add_admission, data_admission)
                    department_num=str(department_num.department_num)
                    cursor.execute("Select total_patient_count from department  where department_num=%s",department_num)
                    dept_det=dictfetchall(cursor)
                    #print >>sys.stderr,dept_det
                    t_count=dept_det[0]["total_patient_count"]+1
                    t_count =str(t_count)
                    cursor.execute("update department set total_patient_count=%s where department_num=%s",(t_count,department_num))
                     
                    cursor.close()
                    return redirect('home')
    else:
        patient_form = PatientForm()
        admitted_form = AdmittedForm()
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    cursor.close() 
    return render(request,'addpatient.html',{'patient_form': patient_form,'admitted_form':admitted_form,'departments':dept_dict})

@login_required
def adddoctor(request):
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST)
        work_for_form =WorksforForm(request.POST)
        cursor = connection.cursor()
        if doctor_form.is_valid() and work_for_form.is_valid()  :
                    #print >>sys.stderr, type(int(request.POST['department_num']))
                    doctor_id = doctor_form.cleaned_data['employee_id']
                    doctor_name = doctor_form.cleaned_data['name']
                    contact_no = doctor_form.cleaned_data['contact_number']
                    grade = doctor_form.cleaned_data['grade']
                    address = doctor_form.cleaned_data['address']
                    starttime = doctor_form.cleaned_data['starttime']
                    endtime = doctor_form.cleaned_data['endtime']
                    add_doctor = ("INSERT INTO doctors  VALUES (%s, %s, %s, %s,%s,%s,%s)")
                    data_doctor = (doctor_id,doctor_name,address,contact_no,grade,starttime,endtime)
                    cursor.execute(add_doctor,data_doctor)
                    department_num = work_for_form.cleaned_data['department']
                    schedule = work_for_form.cleaned_data['schedule']
                    add_workfor = ("INSERT INTO works_for (employee_id,department_num,schedule)  VALUES (%s,%s,%s)")
                    data_workfor = (doctor_id,department_num.department_num,schedule)
                    cursor.execute(add_workfor, data_workfor)
                    department_num=str(department_num.department_num)
                    #print >>sys.stderr,department_num
                    cursor.execute("Select total_worker_count from department  where department_num=%s",department_num)
                    dept_det=dictfetchall(cursor)
                    #print >>sys.stderr,dept_det
                    t_count=dept_det[0]["total_worker_count"]+1
                    t_count =str(t_count)
                    cursor.execute("update department set total_worker_count=%s where department_num=%s",(t_count,department_num))
                    cursor.close()
                    return redirect('home')
    else:
        doctor_form = DoctorForm()
        work_for_form = WorksforForm()
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor) 
    cursor.close() 
    return render(request,'adddoctor.html',{'doctor_form': doctor_form,'work_for_form':work_for_form,'departments':dept_dict})

def displaydoctors(request):
    cursor = connection.cursor()
    cursor.execute("Select * from  doctors NATURAL JOIN works_for  NATURAL JOIN department ")
    doctors=dictfetchall(cursor)
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)    
    cursor.close()
    return render(request,'doctors.html',{'doctors':doctors,'departments':dept_dict})

def displaynurses(request):
    cursor = connection.cursor()
    cursor.execute("Select department_name,name,address from  nurses  NATURAL JOIN department ")
    nurses=dictfetchall(cursor)
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)    
    cursor.close()
    return render(request,'nurses.html',{'nurses':nurses,'departments':dept_dict})

def displayemergency(request):
    cursor = connection.cursor()
    cursor.execute("Select n.name as nurse_name,d.name as name,date from emergency  as e JOIN doctors as d on e.doctor_id=d.employee_id  JOIN nurses as n on n.nurse_id = e.nurse_id ")
    emergency=dictfetchall(cursor)
    # print >>sys.stderr,emergency
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)    
    cursor.close()
    return render(request,'emergency.html',{'emergency':emergency,'departments':dept_dict})
    
def docprofile(request,doc_id):
    cursor = connection.cursor()
    #print >>sys.stderr,type(doc_id),doc_id
    cursor.execute("Select * from  doctors NATURAL JOIN works_for  NATURAL JOIN department where employee_id =%s",[doc_id]);
    doc_profile=dictfetchall(cursor)
    cursor.execute("Select department_num,department_name from department ")
    dept_dict=dictfetchall(cursor)
    #print >>sys.stderr,doc_id
    cursor.close()
    return render(request,'docdetail.html',{'doc_profile':doc_profile,'departments':dept_dict})




def displaydept(request,dept_id):
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    #print >>sys.stderr,type(dept_id),dept_id
    dept_id=str(dept_id)
    cursor.execute("Select * from department  where department_num=%s",[dept_id]);
    dept=dictfetchall(cursor)
    cursor.execute("Select * from  doctors NATURAL JOIN works_for  NATURAL JOIN department where department_num=%s",dept_id);
    doc_dict=dictfetchall(cursor)

    cursor.execute("Select * from  patient NATURAL JOIN admitted  NATURAL JOIN department where department_num=%s",dept_id);
    patients=dictfetchall(cursor)
    # print >>sys.stderr,patients
    cursor.close()
    return render(request,'department-1.html',{'doc_dict':doc_dict,'patients':patients,'departments':dept_dict,'dept':dept})
def contact(request):
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    cursor.close()
    return render(request,'contact.html',{'departments':dept_dict})

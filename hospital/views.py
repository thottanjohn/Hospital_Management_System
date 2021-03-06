# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect,render_to_response
#from .models import Picto,userlike,Profile
from .models import Department,Patient,Nurses,WorksFor,Doctors,Emergency,Admitted
from .forms import DoctorForm,DepartmentForm,PatientForm,WorksforForm,NurseForm,AdmittedForm,EmergencyForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.db import transaction,connection
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
import mysql.connector
import sys
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
                    data_dept = (dept_num,department_name,"0",floor,"0",description)
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
                    data_doctor = (doctor_id,doctor_name,address,contact_no,grade,endtime,starttime)
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
    print >>sys.stderr,emergency
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
    print >>sys.stderr,patients
    cursor.close()
    return render(request,'department-1.html',{'doc_dict':doc_dict,'patients':patients,'departments':dept_dict,'dept':dept})
def contact(request):
    cursor = connection.cursor()
    cursor.execute("Select department_num,department_name from department ");
    dept_dict=dictfetchall(cursor)
    cursor.close()
    return render(request,'contact.html',{'departments':dept_dict})

"""
@login_required
def gallery(request):
        pro=Picto.objects.all()
        count=1
        for p in pro:
            p.liked = p.has_liked(request.user)
            count+=1
        return render(request, 'gallery.html',{'pro':pro,'count':count})

@login_required
def page(request):
    flag=0
    image_id=request.POST['image_id']
    us=Picto.objects.get(pk=image_id)
    users=userlike.objects.filter(image_id=image_id)
    if users.count() !=0:
        for user in users:
            if user.user==request.user:
                flag=1
                if user.favourite==True:
                    user.favourite=False
                    us.like-=1
                    us.save()
                    user.save()
                else:
                    user.favourite=True
                    us.like+=1
                    us.save()
                    user.save()
                break
        if flag!=1:
                user=userlike()
                user.image_id=image_id
                user.user=request.user
                us.like+=1
                us.save()
                user.favourite=True
                user.save()
    else:
        user=userlike()
        user.image_id=image_id
        user.user=request.user
        us.like+=1
        us.save()
        user.favourite=True
        user.save()
    if user.favourite:
        data={'like':us.like,'bol':1}
    else:
        data={'like':us.like,'bol':2}
    return JsonResponse(data)
def events(request):
    return render(request,"events1.html")
@login_required
def view_profile(request):
    likes=0
    snaps=0
    entries=Picto.objects.filter(user=request.user)
    for i in entries:
                likes+=i.like
    snaps=entries.count()   
    args={'user':request.user,'entries':entries,'likes':likes,'snaps':snaps}
    return render(request, 'profile1.html', args)
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def about(request):
    title = "welcome %s" % request.user
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message =form_message
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    return render(request,"about.html",context)
@login_required
@transaction.atomic
def EntryCreate(request):
    if request.method == 'POST':
        user_form = EntryForm(request.POST,request.FILES)
        user_form.user=request.user        
        if user_form.is_valid():            
            cd = user_form.cleaned_data   
            image_field = cd.get('image')            
            img = str(image_field)
            img_name, img_extension = img.split(".")
            image_file = image_file = StringIO.StringIO(image_field.read())
            image = Image.open(image_file)
            width, height = image.size           
            if width > height:
                new_width = 500
                new_height =500
                image = image.resize((new_width, new_height), Image.ANTIALIAS)
              
            else:
                new_height = 500
                new_width = 500
                image = image.resize((new_width, new_height), Image.ANTIALIAS)
            
            image_file = StringIO.StringIO()
            if img_extension == 'JPEG':    
                image.save(image_file, 'JPEG', quality=75)
                
            elif img_extension == 'png':

                image.save(image_file, 'png', quality=75)
                

            elif img_extension == 'bmp':

                image.save(image_file, 'bmp', quality=75)
                

            elif img_extension == 'TIF' or img_extension == 'tif':

                image.save(image_file, 'tiff', quality=75)
                

            elif img_extension == 'tiff':

                image.save(image_file, 'tiff', quality=75)
                

            else:
                image.save(image_file, 'JPEG' ,quality=100)
                

            
        
            
            image_field.file=image_file
            
            
            user_form.save()
            

            
            return redirect('events')


    else:
        user_form = EntryForm()
    return render(request, 'entry.html', {
        'form': user_form,'user':request.user
    })
@login_required
def alt_profile(request,profile_id):
        likes=0
        snaps=0
    	try:
            user = User.objects.get(username=profile_id)
            entries=Picto.objects.filter(user=profile_id)
            for i in entries:
                likes+=i.like
            snaps=entries.count()            

            args={'user':user,'entries':entries,'likes':likes,'snaps':snaps}
        except:
            raise Http404
        return render(request, 'altprofile1.html', args)
@login_required
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message, from_email, ['selfiestreak@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    return render(request, "contact.html", {'form': form})


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})
"""

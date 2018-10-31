# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect,render_to_response
#from .models import Picto,userlike,Profile
from .models import Department
from .forms import DoctorForm,DepartmentForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.db import transaction,connection
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
import mysql.connector
import sys
# Create your views here.


def home(request):
    #title="welcome %s"%request.user
    return render(request,'index.html')
def adddept(request):
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        cursor = connection.cursor()
        if dept_form.is_valid():
                    #print >>sys.stderr, type(int(request.POST['department_num']))
                    dept_num = dept_form.cleaned_data['department_num']
                    #print >>sys.stderr,type(dept_num)
                    department_name = dept_form.cleaned_data['department_name']
                    floor=dept_form.cleaned_data['floor']
                    add_dept = ("INSERT INTO Department  VALUES (%s, %s, %s, %s)")
                    data_dept = (dept_num,department_name,"0",floor)
                    cursor.execute(add_dept, data_dept)
                    cursor.close()
                    return redirect('home')
    else:
        dept_form = DepartmentForm()
    return render(request,'addepartment.html',{'dept_form': dept_form})

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

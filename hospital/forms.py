from django import forms
 
from .models import  Doctors,Department
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.files import File

class DoctorForm(forms.ModelForm):
        class Meta:
            model =Doctors
            fields = ('employee_id','name', 'address', 'contact_number','grade')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_num', 'department_name', 'floor')



            
    
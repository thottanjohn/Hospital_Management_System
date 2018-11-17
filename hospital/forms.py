from django import forms
 
from .models import  Doctors,Department,Nurses,Emergency,WorksFor,Admitted,Patient
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

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id', 'patient_name', 'dt_birth','patient_address')

class AdmittedForm(forms.ModelForm):
    class Meta:
        model =Admitted
        fields = ('department_num', 'date_admission','date_discharge','doctor','prescription','doctor_grade')

class WorksforForm(forms.ModelForm):
    class Meta:
        model = WorksFor
        fields = ('department_num', 'schedule')

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ('nurse_id', 'name', 'address','department_num')

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ('date', 'doctor', 'nurse')



            
    
from django import forms
from django.contrib.admin import widgets
from .models import  Doctors,Department,Nurses,Emergency,WorksFor,Admitted,Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File
import sys
class DateInput(forms.DateInput):
    input_type = 'date'

class DoctorForm(forms.ModelForm):
        class Meta:
            model =Doctors
            fields = ('employee_id','name', 'address', 'contact_number','grade')
        def clean_data(self):
            employee_id = self.cleaned_data['employee_id']
            if employee_id<0:
                return ValidationError('Employee id cannot be negative')
            return 1


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_num', 'department_name', 'floor')
    def clean_data(self):
            employee_id = self.cleaned_data['employee_id']
            if not first_name.isalpha():
                return ValidationError('First name must contain only letters')
            return 1

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id', 'patient_name', 'dt_birth','patient_address')
        widgets = {
            'dt_birth': DateInput()
        }
    def clean_data(self):
            employee_id = self.cleaned_data['employee_id']
            if not employee_id.isalpha():
                return ValidationError('First name must contain only letters')
            return 1
class AdmittedForm(forms.ModelForm):
    class Meta:
        model =Admitted
        fields = ('department_num','date_admission','date_discharge','doctor','prescription')
        widgets = {
            'date_admission': DateInput(),
            'date_discharge': DateInput()
        }
    def clean_data(self):
            employee_id = self.cleaned_data['employee_id']
            if not  employee_id.isalpha():
                return ValidationError('First name must contain only letters')
            return 1

class WorksforForm(forms.ModelForm):
    class Meta:
        model = WorksFor
        fields = ('department_num', 'schedule')
        widgets = {
            'schedule': DateInput(),

        }
    def clean_data(self):
            department_num = self.cleaned_data['employee_id']
            return 1


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ('nurse_id', 'name', 'address','department_num')
    def clean_data(self,nurse_form):
        if nurse_form.is_valid():
            name =nurse_form.cleaned_data['name']
            nurse_id = nurse_form.cleaned_data['nurse_id']
            print >>sys.stderr, nurse_id,name.isalpha()
            if not name.isalpha():
                return ValidationError('Name must contain only letters')
            elif nurse_id<0:
                return ValidationError('Nurse id cannot be negative')
            else:
                return True

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ('date', 'doctor', 'nurse')



            
    
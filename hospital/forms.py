from django import forms
from .models import  Doctors,Department,Nurses,Emergency,WorksFor,Admitted,Patient

import sys
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class DoctorForm(forms.ModelForm):
    class Meta:
            model =Doctors
            fields = ('employee_id','name', 'address', 'contact_number','grade','starttime','endtime')
            widgets = {
            'starttime': TimeInput(),
            'endtime': TimeInput()
        }
    def clean(self):
        cleaned_data = super(DoctorForm, self).clean()
        employee_id= cleaned_data.get('employee_id')
        name = cleaned_data.get('name')
        contact_number = cleaned_data.get('contact_number')
        #print >>sys.stderr,str(contact_number)
        if employee_id<0:
            raise forms.ValidationError('employee_id cannot be negative')
        if not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError('Name must contain only letters')
        if  not contact_number.isdigit():
            raise forms.ValidationError('Contact no should contain only no.s')
        if len(contact_number)!=10:
            raise forms.ValidationError('Contact no must exactly contain 10 digits')
        



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_num', 'department_name', 'floor','description')
    def clean(self):
        cleaned_data = super(DepartmentForm, self).clean()
        department_num= cleaned_data.get('department_num')
        department_name = cleaned_data.get('department_name')
        floor = cleaned_data.get('floor')
        if department_num<0:
            raise forms.ValidationError('department no cannot be negative')
        if not all(x.isalpha() or x.isspace() for x in department_name):
            raise forms.ValidationError('Department name must contain only letters')            
        if floor<0:
            raise forms.ValidationError('Floor no cannot be negative')
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id', 'patient_name', 'dt_birth','patient_address')
        widgets = {
            'dt_birth': DateInput()
        }
    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        patient_id= cleaned_data.get('patient_id')
        patient_name = cleaned_data.get('patient_name')
        if patient_id<0:
            raise forms.ValidationError('patient_id cannot be negative')
        if not all(x.isalpha() or x.isspace() for x in patient_name):
            raise forms.ValidationError('patient_name must contain only letters')  

class AdmittedForm(forms.ModelForm):
    class Meta:
        model =Admitted
        fields = ('department','date_admission','date_discharge','doctor','prescription')
        widgets = {
            'date_admission': DateInput(),
            'date_discharge': DateInput()
        }
    def clean(self):
        cleaned_data = super(AdmittedForm, self).clean()
        date_admission= cleaned_data.get('date_admission')
        date_discharge = cleaned_data.get('date_discharge')
        if date_admission> date_discharge:
            raise forms.ValidationError('Please choose appropriate date of admission and date of discharge')      


class WorksforForm(forms.ModelForm):
    class Meta:
        model = WorksFor
        fields = ('department', 'schedule')
        widgets = {
            'schedule': DateInput(),

        }



class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ('nurse_id', 'name', 'address','department')
    def clean(self):
        cleaned_data = super(NurseForm, self).clean()
        nurse_id= cleaned_data.get('nurse_id')
        name = cleaned_data.get('name')
        if nurse_id<0:
            raise forms.ValidationError('employee_id cannot be negative')
        if not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError('Name must contain only letters')
 

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ('date', 'doctor', 'nurse')
        widgets = {
            'date': DateInput()
        }



            
    
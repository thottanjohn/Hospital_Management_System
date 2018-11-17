# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Doctors(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'doctors'
    def __str__(self):
        return " %s" % self.employee_id
    def __unicode__(self):
        return u" %s" % self.employee_id
class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    dt_birth = models.DateField(blank=True, null=True)
    patient_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'patient'
    def __str__(self):
            return " %s" % self.patient_id
    def __unicode__(self):
        return u" %s" % self.patient_id
class Department(models.Model):
    department_num = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=20)
    total_worker_count=models.IntegerField(blank=True, null=True)
    floor=models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'department'
    def __str__(self):
        return " %s" % self.department_num
    def __unicode__(self):
        return u" %s" % self.department_num

class WorksFor(models.Model):
    department_num = models.ForeignKey(Department, models.DO_NOTHING, db_column='department_num')
    employee = models.ForeignKey(Doctors, models.DO_NOTHING,primary_key=True)
    schedule = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'works_for'
        unique_together = (('department_num', 'employee'),) 

class Admitted(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, primary_key=True)
    department_num = models.ForeignKey(Department, models.DO_NOTHING, db_column='department_num')
    date_admission = models.DateField()
    date_discharge = models.DateField(blank=True, null=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    prescription = models.CharField(max_length=50, blank=True, null=True)
    doctor_grade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'admitted'
        unique_together = (('patient', 'department_num', 'date_admission'),)

class Nurses(models.Model):
    nurse_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True, null=True)
    department_num = models.ForeignKey(Department, models.DO_NOTHING, db_column='department_num')
        
    class Meta:
        db_table = 'nurses'
        unique_together = (('department_num', 'nurse_id'),)

    def __str__(self):
        return " %s" % self.nurse_id
    def __unicode__(self):
        return u" %s" % self.nurse_id

class Emergency(models.Model):
    date = models.DateField(primary_key=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    nurse = models.ForeignKey(Nurses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'emergency'




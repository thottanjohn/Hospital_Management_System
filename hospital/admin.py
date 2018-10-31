# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Doctors,Nurses,Emergency,Department

admin.site.register(Doctors)
admin.site.register(Nurses)
admin.site.register(Emergency)
admin.site.register(Department)



# Register your models here.

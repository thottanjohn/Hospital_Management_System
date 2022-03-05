"""HMS re_path Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import re_path, include
    2. Add a re_path to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from hospital import views as views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #re_path(r'^admin/jsi18n', django.views.i18n.javascript_catalog),
    re_path(r'^$',views.home,name="home"),
    re_path(r'^adddept/$',views.adddept,name="adddept"),
    re_path(r'^addnurse/$',views.addnurse,name="addnurse"),
    re_path(r'^addpatient/$',views.addpatient,name="addpatient"),
    re_path(r'^adddoctor/$',views.adddoctor,name="adddoctor"),
    re_path(r'^addemergency/$',views.addemergency,name="addemergency"),
    re_path(r'^Doctors/$',views.displaydoctors,name="doctors"),
    re_path(r'^Nurses/$',views.displaynurses,name="nurses"),
    re_path(r'^department/(?P<dept_id>[\w\-]*)$', views.displaydept, name='departmentdetail'),
    re_path(r'^doctors/(?P<doc_id>[\w\-]*)$', views.docprofile, name='docdetail'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^contact/',views.contact,name="contact"),
    re_path(r'^emergency/',views.displayemergency,name="displayemergency"),
    ]
"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from hospital import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/jsi18n', django.views.i18n.javascript_catalog),
    url(r'^$',views.home,name="home"),
    url(r'^adddept/$',views.adddept,name="adddept"),
    url(r'^addnurse/$',views.addnurse,name="addnurse"),
    url(r'^addpatient/$',views.addpatient,name="addpatient"),
    url(r'^adddoctor/$',views.adddoctor,name="adddoctor"),
    url(r'^Doctors/$',views.displaydoctors,name="doctors"),
    url(r'^Nurses/$',views.displaynurses,name="nurses"),
    url(r'^department/(?P<dept_id>[\w\-]*)$', views.displaydept, name='departmentdetail'),
    url(r'^doctors/(?P<doc_id>[\w\-]*)$', views.docprofile, name='docdetail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^contact/',views.contact,name="contact"),
    ]
""" 
    url(r'^about/$',views.about,name="about"),  
    url(r'^Greenvibes/add$', views.EntryCreate, name='addentry'),
    url(r'^page/$', views.page, name='pages'),
    url(r'^Greenvibes/page/$', views.gallery, name='detail'),
    url(r'^events/$', views.events, name='events'),   
    url(r'^ContactUs/$', views.contact, name='contact'),  
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/(?P<profile_id>[\w\-]+)$', views.alt_profile, name='altprofile'),
    url(r'^edit$', views.update_profile, name='edit_profile'),
    url(r'^accounts/', include('register.urls')),
    url(r'^Groupfie$', views.upload, name='upload')
    
"""


if settings.DEBUG:
    """urlpatterns += [
        url(r'^generators/', include('django_generators.urls')),

    ]
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
"""
"""CGIDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'dbCGI.views.index'),
    url(r'^hg38IDresult$', 'dbCGI.views.hg38IDresult'),
    url(r'^mm10IDresult$', 'dbCGI.views.mm10IDresult'),
    url(r'^dm3IDresult$', 'dbCGI.views.dm3IDresult'),
    url(r'^ce10IDresult$', 'dbCGI.views.ce10IDresult'),
    url(r'^rn6IDresult$', 'dbCGI.views.rn6IDresult'),
    url(r'^hg38LOCresult$', 'dbCGI.views.hg38LOCresult'),
    url(r'^mm10LOCresult$', 'dbCGI.views.mm10LOCresult'),
    url(r'^dm3LOCresult$', 'dbCGI.views.dm3LOCresult'),
    url(r'^ce10LOCresult$', 'dbCGI.views.ce10LOCresult'),
    url(r'^rn6LOCresult$', 'dbCGI.views.rn6LOCresult'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),    
    url(r'^thanks/$', 'dbCGI.views.thanks', name='thanks'),
    url(r'^$', 'dbCGI.views.contact', name='contact'),
]

#The following enable structural 'static' files while in development mode.
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT, 'show_indexes': True
        }),
        
    )




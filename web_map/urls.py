"""web_map URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

import pcinfo
from map.views import MapMain
from pcinfo.views import PcinfoTable, MainPage, DataGetter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPage.as_view(template_name="index.html")),


    url(r'^data_send/$', DataGetter.as_view(template_name="pcinfo.html")),
    url(r'^list/$', PcinfoTable.as_view(template_name="pcinfo.html")),
    url(r'^list/(?P<sort_id>[0-6]|8)/$', PcinfoTable.as_view(template_name="pcinfo.html")),
    url(r'^support/$', PcinfoTable.as_view(template_name="pcinfo.html")),


    url(r'^map/$', MapMain.as_view(template_name="map.html")),

]

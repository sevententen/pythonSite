from django.conf.urls import *
from pythonSite import connectDB
from pythonSite import login
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
                       (r'^admin/', include(admin.site.urls)),
                       (r'^login/$', login.login),
                       (r'^loginsuccess/$', login.validate),
                       ('^adduser/$', login.adduser),
                       ('^register/$', login.register),
                       ('^showall/$', connectDB.showAll),
                       ('^delete/$', connectDB.delete),
                       )
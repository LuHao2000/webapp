# coding=utf-8
from django.conf.urls import url

# from webapp1.settings import STATIC_ROOT
from . import views

urlpatterns = [
    url(r'^$', views.tologinin),
    url(r'^setadmin/$', views.setadmin),
    url(r'^setuser/$', views.setuser),
    url(r'^toindex/$', views.toindex),
    url(r'^toindex_stu/$', views.toindex_stu),
    url(r'^tologinin/$', views.tologinin),
    url(r'^loginin/$', views.loginin),
    url(r'^loginin/tologinin/$', views.tologinin),
    url(r'^loginin/toindex/$', views.toindex),
    url(r'^loginin/toindex_stu/$', views.toindex_stu),
    url(r'^loginin/index/$', views.index),
    url(r'^loginin/index_stu/$', views.index_stu),
    url(r'^loginin/chart12/$', views.chart12),
    url(r'^loginin/tosecurity/$', views.tosecurity),
    url(r'^chart12/$', views.chart12),
    url(r'^register/$', views.register),
    url(r'^toregister/$', views.toregister),
    url(r'^toregister/register/$', views.register),
    url(r'^loginin/user_index/$', views.index),
    url(r'^loginin/user_index_16/$', views.index16),
    url(r'^loginin/user_index_17/$', views.index17),
    url(r'^loginin/user_index_stu/$', views.index_stu),
    url(r'^loginin/user_index_16_stu/$', views.index16_stu),
    url(r'^loginin/user_index_17_stu/$', views.index17_stu),

    url(r'^index/$', views.index),
    url(r'^index16/$', views.index16),
    url(r'^index17/$', views.index17),
    url(r'^index_stu/$', views.index_stu),
    url(r'^index16_stu/$', views.index16_stu),
    url(r'^index17_stu/$', views.index17_stu),

    url(r'^add/$', views.add),
    url(r'^add16/$', views.add16),
    url(r'^add17/$', views.add17),

    url(r'^loginin/add/$', views.add),
    url(r'^loginin/add16/$', views.add16),
    url(r'^loginin/add17/$', views.add17),

    url(r'^edit/$', views.edit),
    url(r'^edit16/$', views.edit16),
    url(r'^edit17/$', views.edit17),
    url(r'^loginin/edit/$', views.edit),
    url(r'^loginin/edit16/$', views.edit16),
    url(r'^loginin/edit17/$', views.edit17),

    url(r'^findStudent_stu/$', views.findStudent_stu),
    url(r'^findStudent16_stu/$', views.findStudent16_stu),
    url(r'^findStudent17_stu/$', views.findStudent17_stu),
    url(r'^findStudent/$', views.findStudent),
    url(r'^findStudent16/$', views.findStudent16),
    url(r'^findStudent17/$', views.findStudent17),

    url(r'^findStudent/edit/$', views.edit),
    url(r'^findStudent16/edit16/$', views.edit16),
    url(r'^findStudent17/edit17/$', views.edit17),

    url(r'^delete/$', views.delete),
    url(r'^delete16/$', views.delete16),
    url(r'^delete17/$', views.delete17),
    url(r'^loginin/delete/$', views.delete),
    url(r'^loginin/delete16/$', views.delete16),
    url(r'^loginin/delete17/$', views.delete17),
    url(r'^findStudent/delete/$', views.delete),
    url(r'^findStudent16/delete16/$', views.delete16),
    url(r'^findStudent17/delete17/$', views.delete17),

    url(r'^loginin/user_index/$', views.findStudent),
    url(r'^loginin/user_index_16/$', views.findStudent16),
    url(r'^loginin/user_index_17/$', views.findStudent17),
    url(r'^loginin/user_index_stu/$', views.findStudent_stu),
    url(r'^loginin/user_index_16_stu/$', views.findStudent16_stu),
    url(r'^loginin/user_index_17_stu/$', views.findStudent17_stu),

    url(r'^loginin/findStudent/$', views.findStudent),
    url(r'^loginin/findStudent16/$', views.findStudent16),
    url(r'^loginin/findStudent17/$', views.findStudent17),
    url(r'^loginin/findStudent_stu/$', views.findStudent_stu),
    url(r'^loginin/findStudent16_stu/$', views.findStudent16_stu),
    url(r'^loginin/findStudent17_stu/$', views.findStudent17_stu),

    url(r'^tosecurity/$', views.tosecurity),
    url(r'^tosecurity/security/$', views.security),
    url(r'^tosecurity/security/newpw_set/$', views.newpw_set),

]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
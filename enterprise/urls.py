from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.toshow),
    url(r'^addEmp$', views.addEmp),
    # url(r'^$',)
    url(r'^tomessage$', views.tomessage),
    url(r'^toinfo$', views.toinfo),
    url(r'^toinfo-edit$', views.toinfo_edit),
    url(r'^torelease$', views.torelease),
    url(r'^tocontent$', views.tocontent),
    url(r'^torelated$', views.torelated),
    url(r'^indexEmp$', views.indexEmp),
    url(r'^tostanderd$', views.tostanderd),
    url(r'^editEnter/$', views.editEnter),
    url(r'^deleteEmp/$', views.deleteEmp),
    url(r'^editEmp/$', views.editEmp),
    url(r'^editEmp/editEmp/$', views.editEmp),
    url(r'^toshow$', views.toshow),
]
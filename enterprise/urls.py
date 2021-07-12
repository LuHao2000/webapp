from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.toinfo),
    # url(r'^$',)
    url(r'^tomessage$', views.tomessage),
    url(r'^toinfo$', views.toinfo),
    url(r'^toinfo-edit$', views.toinfo_edit),
    url(r'^torelease$', views.torelease),
    url(r'^tocontent$', views.tocontent),
    url(r'^torelated$', views.torelated),
    url(r'^toindex$', views.toindex),
    url(r'^tostanderd$', views.tostanderd),
]
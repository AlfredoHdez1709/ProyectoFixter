from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
	url(r'^Administrador$', views.Panel.as_view(), name="list"),
	url(r'^registro/$', views.Registro.as_view(),name="registro"),
]
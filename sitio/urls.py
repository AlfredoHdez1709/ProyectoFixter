from django.conf.urls import url,include
from django.contrib import admin
from Administrador import urls as AdministradorUrls
from Principal import urls as PrincipalUrls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(AdministradorUrls)),
    url(r'^',include(PrincipalUrls)),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	)
]

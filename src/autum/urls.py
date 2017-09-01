from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from cloud.views import home, contact, dashboard, about, acknowledgement, support, migration, monitor, cpfinal, instance
from inmate_admin.views import inmate

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^acknowledgement/$', acknowledgement, name='acknowledgement'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^cpfinal/$', cpfinal, name='cpfinal'),
    url(r'^support/$', support, name='support'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^inmate/$', inmate, name='inmate')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from cloud.views import home, contact, dashboard, about, acknowledgement, support, migration, monitor, cpfinal, instance
from aws.views import aws, aws_home
from azure.views import azure
from ibm.views import ibm

from google.views import google
from rackspace.views import rackspace


urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^acknowledgement/$',acknowledgement,name='acknowledgement'),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    # url(r'^cp_final/$', cp_final, name='cp_final'),
    url(r'^cpfinal/$', cpfinal , name='cpfinal'),
    url(r'^aws/$',aws,name='aws'),
    url(r'^aws_home/$',aws_home,name='aws_home'),
    url(r'^azure/$',azure,name='azure'),
    # url(r'^Azure_Home/$',azure_home,name='azure'),
    url(r'^ibm/$',ibm,name='ibm'),
    # url(r'^IBM_Home/$',ibm_home,name='ibm'),
    url(r'^google/$',google,name='google'),
    # url(r'^Google_Home/$',google_home,name='google'),
    url(r'^rackspace/$',rackspace,name='rackspace'),
    # url(r'^Rackspace_Home/$',rackspace_home,name='rackspace'),
    url(r'^support/$',support,name='support'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^migration/$',migration,name='migration'),
    url(r'^monitor/$',monitor,name='monitor'),
    url(r'^instance/$', instance, name='instance'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	

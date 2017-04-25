from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from cloud.views import home, contact, dashboard, about, acknowledgement, support, migration, monitor, cpfinal, instance

from aws.views import aws, aws_home, aws_delete, aws_create
from azure.views import azure, azure_home
from ibm.views import ibm

from google.views import google, google_create, google_retrieve, google_delete, google_home
from rackspace.views import rackspace, rackspace_create, rackspace_home, rackspace_update, rackspace_delete



urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^acknowledgement/$',acknowledgement,name='acknowledgement'),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    # url(r'^cp_final/$', cp_final, name='cp_final'),
    url(r'^cpfinal/$', cpfinal , name='cpfinal'),
    url(r'^aws/$',aws,name='aws'),
    url(r'^aws_create/$',aws_create,name='aws_create'),
    url(r'^aws_home/$', aws_home, name='aws_home'),
    url(r'^aws_delete/$', aws_delete, name='aws_delete'),
    url(r'^azure/$',azure,name='azure'),
    # url(r'^Azure_Home/$',azure_home,name='azure'),
    url(r'^azure_home/$',azure_home,name='azure_home'),
    url(r'^ibm/$',ibm,name='ibm'),
    # url(r'^IBM_Home/$',ibm_home,name='ibm'),
    url(r'^google/$',google,name='google'),
    url(r'^google_home/$',google_home,name='google_home'),
    url(r'^google_create/$',google_create,name='google_create'),
    url(r'^google_retrieve/$', google_retrieve, name='google_retrieve'),
    url(r'^google_delete/$', google_delete, name='google_delete'),
    url(r'^rackspace/$',rackspace,name='rackspace'),
    url(r'^rackspace_create/$',rackspace_create,name='rackspace_create'),
    url(r'^rackspace_home/$', rackspace_home, name='rackspace_home'),
    url(r'^rackspace_update/$',rackspace_update,name='rackspace_update'),
    url(r'^rackspace_delete/$',rackspace_delete,name='rackspace_delete'),
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
	

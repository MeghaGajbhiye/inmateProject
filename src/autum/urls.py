from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from cloud.views import home, contact, dashboard, about, acknowledgement, support, migration, monitor, cpfinal, instance
from aws.views import aws, aws_home, aws_inst, aws_delete, aws_create
from azure.views import azure, azure_inst
from ibm.views import ibm

from google.views import google, google_home
from rackspace.views import rackspace, rackspace_home


urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^acknowledgement/$',acknowledgement,name='acknowledgement'),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    # url(r'^cp_final/$', cp_final, name='cp_final'),
    url(r'^cpfinal/$', cpfinal , name='cpfinal'),
    url(r'^aws/$',aws,name='aws'),
    url(r'^aws_home/$',aws_home,name='aws_home'),
    url(r'^aws_inst/$', aws_inst, name='aws_inst'),
    url(r'^aws_delete/$', aws_delete, name='aws_delete'),
    url(r'^aws_create/$', aws_create, name='aws_create'),
    url(r'^azure/$',azure,name='azure'),
    # url(r'^Azure_Home/$',azure_home,name='azure'),
    url(r'^azure_inst/$',azure_inst,name='azure_inst'),
    url(r'^ibm/$',ibm,name='ibm'),
    # url(r'^IBM_Home/$',ibm_home,name='ibm'),
    url(r'^google/$',google,name='google'),
    url(r'^google_home/$',google_home,name='google_home'),
    url(r'^rackspace/$',rackspace,name='rackspace'),
    url(r'^rackspace_home/$',rackspace_home,name='rackspace_home'),
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
	

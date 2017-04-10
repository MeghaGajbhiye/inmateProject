from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from cloud.views import home, contact, dashboard, about
from aws.views import aws, aws_home
from azure.views import azure
from ibm.views import ibm
from google.views import google
from rackspace.views import rackspace


urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    url(r'^aws/$',aws,name='aws'),
    url(r'^AWS_Home/$',aws_home,name='aws'),
    url(r'^azure/$',azure,name='azure'),
    url(r'^ibm/$',ibm,name='ibm'),
    url(r'^google/$',google,name='google'),
    url(r'^rackspace/$',rackspace,name='rackspace'),
    url(r'^about/$',about,name='about'),
    

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	

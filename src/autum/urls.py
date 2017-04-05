from django.conf.urls import include, url
from django.contrib import admin
from cloud.views import home, contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact/$', 'cloud.views.contact', name='contact'),
    url(r'^dashboard/$','cloud.views.dashboard',name='dashboard'),
    url(r'^aws/$','cloud.views.aws',name='aws'),
    url(r'^dashboard/azure/$','cloud.views.azure',name='azure'),
    url(r'^dashboard/ibm/$','cloud.views.ibm',name='ibm'),
    url(r'^dashboard/google/$','cloud.views.google',name='google'),
    url(r'^dashboard/rackspace/$','cloud.views.rackspace',name='rackspace'),
    url(r'^about/$','cloud.views.about',name='about'),
    

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	

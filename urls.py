from django.conf.urls import include, url
from django.contrib import admin
from cloud.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact/$', 'cloud.views.contact', name='contact'),
    url(r'^dashboard/$','cloud.views.dashboard',name='dashboard'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	
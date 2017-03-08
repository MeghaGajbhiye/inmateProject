from django.conf.urls import include, url
from django.contrib import admin
from cloud.views import home, contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact/', contact, name= 'contact'), 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	
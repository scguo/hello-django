from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static  

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'mysite.views.landing',name='landing'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
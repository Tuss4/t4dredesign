from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'tuss4.views.main'),
	url(r'^about/$','pages.views.about'),
	url(r'^contact/$','pages.views.contact'),
	url(r'^portfolio/$','pages.views.portfolio'),
	url(r'^videos/$','pages.views.videos'),
	url(r'^repos/$', 'pages.views.repos')
    # Examples:
    # url(r'^$', 'tuss4.views.home', name='home'),
    # url(r'^tuss4/', include('tuss4.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
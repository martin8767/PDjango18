from django.conf.urls import include, url
from django.contrib import admin
#from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
] ##

if settings.DEBUG:  ## en development lo ponemos en false y se activa
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.static_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.static_ROOT)
    pass

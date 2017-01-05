from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', 'lecciones.views.homel', name='homel'),

    url(r'^leccion1/vocabulario', 'lecciones.views.leccion1vocabulario', name='leccion1v'),
    url(r'^leccion2/vocabulario', 'lecciones.views.leccion2vocabulario', name='leccion2v'),
    url(r'^leccion3/vocabulario', 'lecciones.views.leccion3vocabulario', name='leccion3v'),
    url(r'^leccion4/vocabulario', 'lecciones.views.leccion4vocabulario', name='leccion4v'),
    


    # url(r'^blog/', include('blog.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', 'lecciones.views.homel', name='homel'),

    url(r'leccion1', 'lecciones.views.leccion1', name='leccion1'),


    # url(r'^blog/', include('blog.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

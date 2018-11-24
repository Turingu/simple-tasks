from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework_swagger.views import get_swagger_view

from apps.accounts.urls import urlpatterns as accounts_urlpatterns
from apps.tasks.api.urls import urlpatterns as tasks_urlpatterns

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    #url('', include('tasks.api.urls')), #r'^api/'
    url(r'^schema/$', schema_view),
]

urlpatterns += accounts_urlpatterns
urlpatterns += tasks_urlpatterns

if settings.DEBUG:
    from django.conf.urls.static import static

    # Serve static and media files from development server
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Simple Tasks Admin'

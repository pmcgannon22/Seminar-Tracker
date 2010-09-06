from django.conf.urls.defaults import *
from django.conf import settings
from tracker import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Seminar_Django/', include('Seminar_Django.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT , 'show_indexes': True}),
    (r'^$', views.index),
)

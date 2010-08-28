from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Seminar_Django.tracker import views
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Seminar_Django/', include('Seminar_Django.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^test/$',views.test_veiw),
)

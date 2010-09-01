from django.conf.urls.defaults import *
from django.contrib import admin
from Seminar_Django.tracker import views
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login , {'template_name' : 'login.dhtml'}),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', views.roster),
    (r'^test/$',views.test_veiw),
)

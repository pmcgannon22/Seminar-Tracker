from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
from Seminar_Django.tracker import views
from Seminar_Django import settings


admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT , 'show_indexes': True }),
    (r'^admin/', include(admin.site.urls)),   
    (r'^test/$',views.test_veiw),
    (r'^accounts/$', views.home),
    (r'^accounts/login/$',  login , {'template_name' : 'login.dhtml'}),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', views.roster),

)

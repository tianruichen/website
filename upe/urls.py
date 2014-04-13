from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^officehours/$', 'website.views.officehours', name='officehours'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'website.views.register', name='register'),
    url(r'^thanks/$', 'website.views.register_thanks', name='register_thanks'),
    url(r'^login/$', 'website.views.login', name='login'),
)

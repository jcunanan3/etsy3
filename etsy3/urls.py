from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'etsy3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','etsy3_app.views.index', name='index'),
    url(r'^show_shop/$','etsy3_app.views.show_shop', name='show_shop'),
    url(r'^show_faves/$','etsy3_app.views.show_faves', name='show_faves'),
    url(r'^index2/$','etsy3_app.views.index2', name='index2'),
)

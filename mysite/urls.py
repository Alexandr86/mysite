from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from blog.views import PersonListView, PortfolioListView, ContactsCreateView
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/blog/')),
    url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^portfolio/', PortfolioListView.as_view()),
    url(r'^resume/', PersonListView.as_view()),
    url(r'^contacts/$', ContactsCreateView.as_view()),
    # url(r'^$', 'mysite.blog.views', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),


    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

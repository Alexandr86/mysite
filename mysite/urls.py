from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from blog.views import PersonListView, PortfolioListView, ContactsCreateView, ContactViewSet, UserViewSet, GroupViewSet
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

# class UserViewSet(viewsets.ModelViewSet):
#     model = User
#
# class GroupViewSet(viewsets.ModelViewSet):
#     model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='/blog/')),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^portfolio/', PortfolioListView.as_view()),
                       url(r'^resume/', PersonListView.as_view()),
                       url(r'^contacts/$', ContactsCreateView.as_view()),
                       url(r'^sentry/', include('sentry.web.urls')),
                       url(r'^rest/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


                       # url(r'^$', 'mysite.blog.views', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),


                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

)

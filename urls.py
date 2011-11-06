from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import Post
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djblog.views.home', name='home'),
    # url(r'^djblog/', include('djblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  (r'^', include('blog.urls')),  
  url(r'^admin/', include(admin.site.urls)),
  url(r'(?P<slug>[a-zA-Z0-9_.-]+)/$',
      DetailView.as_view(
        model=Post,
        template_name='blog/post_detail.html'),
      name='single_post'),
)

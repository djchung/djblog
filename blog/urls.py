from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, date_based, TemplateView
from blog.models import Post, Inspiration, About

info_dict = {
  'queryset': Post.objects.all(),
  'date_field': 'published',
  
}
urlpatterns = patterns('',
  (r'^$',
    ListView.as_view(
      queryset=Post.objects.order_by('-published')[:3],
      context_object_name='post_list',
      template_name='blog/index.html')),
  (r'^about/',
    ListView.as_view(
    queryset=About.objects.all(),
    context_object_name='about_list',
    template_name='blog/about.html')),
  (r'^archive/$',
    ListView.as_view(
    queryset=Post.objects.order_by('-published'),
    context_object_name='post_list',
    template_name='blog/archive.html')),
  (r'^inspiration/$',
   ListView.as_view(
    queryset=Inspiration.objects.all(),
    context_object_name='quote_list',
    template_name='blog/inspiration.html')),
  (r'^contact/', 'blog.views.contact'),
  (r'^thanks/', TemplateView.as_view(template_name='blog/thanks.html')),
  )
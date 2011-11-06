from django.views.generic import TemplateView
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render_to_response

def archive(request):
  posts = Post.objects.all()

class AboutView(TemplateView):
  template_name = "blog/about.html"



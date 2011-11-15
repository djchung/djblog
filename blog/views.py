from django.views.generic import TemplateView
from blog.models import Post, ContactForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.core.mail import send_mail
from django.core.context_processors import csrf

def archive(request):
  posts = Post.objects.all()

class AboutView(TemplateView):
  template_name = "blog/about.html"

def contact(request):
  c = RequestContext(request)
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      # email message to me
      subject = 'message from ' + form.cleaned_data['name']
      message = form.cleaned_data['message']
      sender = 'hairplaza@gmail.com'
      to = ['djchung3@gmail.com']
      send_mail(subject, message, sender, to)
      return HttpResponseRedirect('/thanks/')
  else:
    form = ContactForm()
    
  return render_to_response('blog/contact.html', { 'form' : form, }, c)


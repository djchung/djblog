from django.contrib import admin
from blog.models import Category, Post, Inspiration, About

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Inspiration)
admin.site.register(About)
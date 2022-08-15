from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Categories, Post, Profile, Comment

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Profile)
admin.site.register(Comment)
# Register your models here.

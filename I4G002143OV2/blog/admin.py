from django.contrib import admin
from .models import Post, Title, Slug, Update, Create, Author, Body, Publish, Status

# Register your models here.

admin.site.register(Post)
admin.site.register(Title)
admin.site.register(Slug)
admin.site.register(Update)
admin.site.register(Create)
admin.site.register(Author)
admin.site.register(Body)
admin.site.register(Publish)
admin.site.register(Status)
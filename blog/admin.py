from django.contrib import admin
from .models import Post
# Register your models here.


# edit
# admin.site.register(Post)

class Post_ed(admin.ModelAdmin):
    list_display = ['post_title','post_value', 'activate']
    search_fields = ['post_title']
    list_editable = ['activate']

admin.site.register(Post, Post_ed)
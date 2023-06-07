from django.contrib import admin
from apps.blog.models import Chef, About, Post, Comment
from django.utils.html import format_html


class PostAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'category',
                    'title', 'author')
    list_display_links = ('id', 'title', 'thumbnail')
    search_fields = ('title', 'writer', 'body')


class ChefAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name', 'role')
    list_display_links = ('id', 'name', 'thumbnail')
    search_fields = ('name', 'role')


admin.site.register(Chef, ChefAdmin)
admin.site.register(About)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

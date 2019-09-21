from django.contrib import admin
from webapp.models import Book


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status','text','email']
    list_filter = ['status']
    list_display_links = ['pk',]
    search_fields = ['text']
    fields = ['name','email', 'text', 'status',]


admin.site.register(Book, ArticleAdmin)

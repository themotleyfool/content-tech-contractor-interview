from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']


admin.site.register(Article, ArticleAdmin)

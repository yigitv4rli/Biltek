from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)
admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','date')
    list_display_links = ('title','date')
    search_fields = ('title')
    list_filter = ('date')

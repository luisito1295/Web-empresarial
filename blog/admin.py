from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author')
    ordering = ('author',)
    search_fields = ('title','author__username', 'categories__name')
    date_hierarchy = ('published')
    list_filter = ('author__username', 'categories__name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


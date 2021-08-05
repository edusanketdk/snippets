from django.contrib import admin
from .models import blog

class blogAdminView(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title')}

admin.site.register(blog)

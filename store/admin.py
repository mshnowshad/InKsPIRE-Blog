from django.contrib import admin
from .models import PostModel,Category

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'title', 'published_in')  # Add 'id' here
    list_display_links = ('id', 'title')  # Ensure 'id' is in list_display_links
    list_filter = ('title', 'author')
    search_fields = ('title', 'author', 'description')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Category)




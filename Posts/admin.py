from django.contrib import admin
from .models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'content',
        'publish_date',
    ]
    list_filter = [
        'title',
        'content',
        'publish_date',
    ]
    search_fields = [
        'title',
        'content',
        'publish_date',
    ]

admin.site.register(Posts, PostAdmin)

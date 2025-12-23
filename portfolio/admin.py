from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_featured', 'project_date', 'views', 'order']
    list_filter = ['status', 'is_featured', 'technologies']
    list_editable = ['order', 'is_featured', 'status']
    search_fields = ['title', 'short_description', 'full_description']
    filter_horizontal = ['technologies']
    readonly_fields = ['views', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'full_description')
        }),
        ('Media', {
            'fields': ('featured_image', 'screenshots')
        }),
        ('Technologies & Links', {
            'fields': ('technologies', 'github_url', 'live_url', 'demo_video_url')
        }),
        ('Metadata', {
            'fields': ('status', 'is_featured', 'order', 'project_date')
        }),
    )

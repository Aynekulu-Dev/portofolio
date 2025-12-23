# core/admin.py (Complete version)
from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, Technology

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'email', 'phone', 'updated_at', 'preview_link']
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_description', 'site_logo', 'favicon')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'email', 'phone')
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id',)
        }),
    )
    
    def preview_link(self, obj):
        return format_html('<a href="/" target="_blank">View Site</a>')
    preview_link.short_description = 'Preview'
    
    def has_add_permission(self, request):
        # Only allow one SiteSettings instance
        return not SiteSettings.objects.exists()

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color_display', 'order', 'project_count']
    list_editable = ['order']
    search_fields = ['name']
    list_filter = ['projects']
    
    def color_display(self, obj):
        return format_html(
            '<div style="display: flex; align-items: center; gap: 8px;">'
            '<div style="width: 20px; height: 20px; background: {}; border-radius: 4px;"></div>'
            '<span>{}</span>'
            '</div>',
            obj.color,
            obj.color
        )
    color_display.short_description = 'Color'
    
    def project_count(self, obj):
        return obj.projects.count()
    project_count.short_description = 'Projects'
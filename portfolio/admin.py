from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Project

# Custom form to prevent auto-selection
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Clear initial selection for new projects
        if not self.instance.pk:
            self.initial['technologies'] = []

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['title', 'status', 'is_featured', 'project_date', 'views', 'order', 'technology_list']
    list_filter = ['status', 'is_featured', 'technologies']
    list_editable = ['order', 'is_featured', 'status']
    search_fields = ['title', 'short_description', 'full_description']
    raw_id_fields = ['technologies']  # This shows a search/popup widget
    readonly_fields = ['views', 'created_at', 'updated_at', 'thumbnail_preview']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'full_description')
        }),
        ('Media', {
            'fields': ('featured_image', 'thumbnail_preview', 'screenshots')
        }),
        ('Technologies & Links', {
            'fields': ('technologies', 'github_url', 'live_url', 'demo_video_url')
        }),
        ('Metadata', {
            'fields': ('status', 'is_featured', 'order', 'project_date')
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj.featured_image:
            return format_html(f'<img src="{obj.featured_image.url}" style="width: 100px; height: 100px; object-fit: cover;" />')
        return "No image"
    thumbnail_preview.short_description = "Featured Image Preview"
    
    def technology_list(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])
    technology_list.short_description = 'Technologies'
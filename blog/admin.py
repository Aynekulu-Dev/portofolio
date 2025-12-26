from django.contrib import admin
from django.utils.html import format_html
from .models import BlogCategory, BlogPost

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'post_count']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    
    def post_count(self, obj):
        return obj.blogpost_set.count()
    post_count.short_description = 'Posts'

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'author', 'published_date', 'views', 'is_featured', 'reading_time']
    list_filter = ['status', 'is_featured', 'category', 'tags', 'published_date']
    list_editable = ['status', 'is_featured', 'reading_time']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'created_at', 'updated_at', 'published_date', 'thumbnail_preview']  # FIXED HERE
    date_hierarchy = 'published_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Media', {
            'fields': ('featured_image', 'thumbnail_preview')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Publication', {
            'fields': ('status', 'is_featured', 'published_date', 'allow_comments', 'reading_time')
        }),
        ('Author', {
            'fields': ('author',)
        }),
        ('Statistics', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj.featured_image:
            return format_html(f'<img src="{obj.featured_image.url}" style="width: 100px; height: 100px; object-fit: cover;" />')
        return "No image"
    thumbnail_preview.short_description = "Featured Image Preview"
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
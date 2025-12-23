from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status_badge', 'created_at', 'admin_actions']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'ip_address', 'user_agent', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_replied', 'mark_as_spam']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Technical Information', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Status Management', {
            'fields': ('status', 'admin_notes', 'responded_at')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def status_badge(self, obj):
        status_colors = {
            'new': 'red',
            'read': 'blue',
            'replied': 'green',
            'spam': 'gray',
        }
        color = status_colors.get(obj.status, 'gray')
        return format_html(
            '<span style="background: {}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px;">{}</span>',
            color,
            obj.get_status_display().upper()
        )
    status_badge.short_description = 'Status'
    
    def admin_actions(self, obj):
        return format_html(
            '<div style="display: flex; gap: 5px;">'
            '<a href="mailto:{}?subject=Re: {}" style="background: #4CAF50; color: white; padding: 3px 8px; border-radius: 4px; text-decoration: none;">Reply</a>'
            '<a href="/admin/contact/contactsubmission/{}/change/" style="background: #2196F3; color: white; padding: 3px 8px; border-radius: 4px; text-decoration: none;">View</a>'
            '</div>',
            obj.email,
            obj.subject,
            obj.id
        )
    admin_actions.short_description = 'Actions'
    
    def mark_as_read(self, request, queryset):
        queryset.update(status='read')
        self.message_user(request, f"{queryset.count()} submissions marked as read.")
    mark_as_read.short_description = "Mark selected as read"
    
    def mark_as_replied(self, request, queryset):
        queryset.update(status='replied', responded_at=timezone.now())
        self.message_user(request, f"{queryset.count()} submissions marked as replied.")
    mark_as_replied.short_description = "Mark selected as replied"
    
    def mark_as_spam(self, request, queryset):
        queryset.update(status='spam')
        self.message_user(request, f"{queryset.count()} submissions marked as spam.")
    mark_as_spam.short_description = "Mark selected as spam"
    
    def has_add_permission(self, request):
        return False
    
    def save_model(self, request, obj, form, change):
        if obj.status == 'replied' and not obj.responded_at:
            obj.responded_at = timezone.now()
        super().save_model(request, obj, form, change)

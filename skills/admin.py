from django.contrib import admin
from django.utils.html import format_html
from .models import SkillCategory, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'level', 'percentage', 'icon', 'order', 'is_active']
    ordering = ['order']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order', 'skill_count']
    list_editable = ['order']
    search_fields = ['name', 'description']
    inlines = [SkillInline]
    
    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = 'Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level_display', 'percentage', 'icon', 'years_experience', 'order', 'is_active']
    list_filter = ['category', 'level', 'is_active']
    list_editable = ['percentage', 'order', 'is_active', 'years_experience']
    search_fields = ['name', 'description']
    ordering = ['category__order', 'order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Skill Details', {
            'fields': ('level', 'percentage', 'years_experience', 'icon')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def level_display(self, obj):
        level_colors = {
            1: 'gray',
            2: 'blue',
            3: 'green',
            4: 'purple',
        }
        color = level_colors.get(obj.level, 'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_level_display()
        )
    level_display.short_description = 'Level'

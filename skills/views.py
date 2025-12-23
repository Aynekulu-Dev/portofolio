from django.shortcuts import render
from django.views.generic import ListView
from .models import SkillCategory, Skill

class SkillListView(ListView):
    model = SkillCategory
    template_name = 'skills/skill_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return SkillCategory.objects.prefetch_related('skills').all().order_by('order')

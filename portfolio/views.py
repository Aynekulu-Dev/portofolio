from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        return Project.objects.filter(status='completed').order_by('-order', '-created_at')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_object(self):
        obj = super().get_object()
        obj.increment_views()  # Track views
        return obj

def project_by_technology(request, tech_id):
    """View projects by technology"""
    projects = Project.objects.filter(technologies__id=tech_id, status='completed')
    return render(request, 'portfolio/project_list.html', {'projects': projects})

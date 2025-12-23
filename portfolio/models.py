from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from core.models import Technology

class Project(models.Model):
    """Portfolio projects"""
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    
    # Media
    featured_image = models.ImageField(upload_to='projects/')
    screenshots = models.TextField(help_text="Comma-separated image paths", blank=True)
    
    # Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    demo_video_url = models.URLField(blank=True)
    
    # Metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_date = models.DateField()
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})
    
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    def get_screenshots_list(self):
        if self.screenshots:
            return [img.strip() for img in self.screenshots.split(',')]
        return []
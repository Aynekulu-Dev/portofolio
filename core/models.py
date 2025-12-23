from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

class SiteSettings(models.Model):
    """Global site settings"""
    site_name = models.CharField(max_length=100, default="DevPortfolio Pro")
    site_description = models.TextField(default="Modern Developer Portfolio")
    site_logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Social Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    
    # Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name

class Technology(models.Model):
    """Technology tags for projects"""
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="Font Awesome class name")
    color = models.CharField(max_length=7, default="#000000", help_text="Hex color code")
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
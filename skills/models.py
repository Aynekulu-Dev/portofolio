from django.db import models

class SkillCategory(models.Model):
    """Skill categories (Backend, Frontend, DevOps, etc.)"""
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="Font Awesome class")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    """Individual skills"""
    LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    percentage = models.IntegerField(default=0, help_text="0-100")
    icon = models.CharField(max_length=100, help_text="Font Awesome class")
    description = models.TextField(blank=True)
    years_experience = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
    
    def get_percentage_display(self):
        """Calculate percentage based on level"""
        if self.percentage > 0:
            return self.percentage
        level_percentages = {1: 30, 2: 60, 3: 85, 4: 100}
        return level_percentages.get(self.level, 0)
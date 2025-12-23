from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogCategory

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(status='published').order_by('-published_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = BlogPost.objects.filter(
            status='published', 
            is_featured=True
        ).order_by('-published_date')[:2]
        return context

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_object(self):
        obj = super().get_object()
        obj.increment_views()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # Get related posts by tags or category
        related_posts = BlogPost.objects.filter(
            status='published',
            tags__in=post.tags.all()
        ).exclude(id=post.id).distinct()[:2]
        
        if not related_posts.exists():
            related_posts = BlogPost.objects.filter(
                status='published',
                category=post.category
            ).exclude(id=post.id)[:2]
        
        # Get next and previous posts
        previous_post = BlogPost.objects.filter(
            status='published',
            published_date__lt=post.published_date
        ).order_by('-published_date').first()
        
        next_post = BlogPost.objects.filter(
            status='published',
            published_date__gt=post.published_date
        ).order_by('published_date').first()
        
        context['related_posts'] = related_posts
        context['previous_post'] = previous_post
        context['next_post'] = next_post
        return context

class BlogCategoryView(ListView):
    model = BlogPost
    template_name = 'blog/category_detail.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(BlogCategory, slug=self.kwargs['slug'])
        return BlogPost.objects.filter(
            category=self.category, 
            status='published'
        ).order_by('-published_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

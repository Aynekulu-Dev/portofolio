from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='post_list'),
    path('category/<slug:slug>/', views.BlogCategoryView.as_view(), name='category_detail'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='post_detail'),
]

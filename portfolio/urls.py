from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('technology/<int:tech_id>/', views.project_by_technology, name='project_by_tech'),
]

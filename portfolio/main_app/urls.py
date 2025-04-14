# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('contact/', views.contact, name='contact'),
    path('achievements/', views.achievements, name='achievements'),
]

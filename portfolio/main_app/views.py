# main_app/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Project, Experience, Education, Achievement
from .forms import ContactForm
from itertools import chain
from django.db.models import F,Q
from django.db import models

class HomeView(TemplateView):
    template_name = 'main_app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(is_featured=True).order_by('order')[:3]
        context['skills'] = Skill.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'main_app/about.html'

class SkillsView(ListView):
    model = Skill
    template_name = 'main_app/skills.html'
    context_object_name = 'skills'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['backend_skills'] = Skill.objects.filter(category='BACKEND')
        context['frontend_skills'] = Skill.objects.filter(category='FRONTEND')
        context['database_skills'] = Skill.objects.filter(category='DATABASE')
        context['other_skills'] = Skill.objects.filter(~Q(category__in=['BACKEND', 'FRONTEND', 'DATABASE']))
        return context

class ProjectsView(ListView):
    model = Project
    template_name = 'main_app/projects.html'
    context_object_name = 'projects'
    ordering = ['order']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'main_app/project_detail.html'
    context_object_name = 'project'

class ExperienceView(TemplateView):
    template_name = 'main_app/experience.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all().order_by('-start_date')
        context['education'] = Education.objects.all().order_by('-graduation_date')
        return context

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Email body
            email_message = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            
            try:
                # Send email
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=email_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
    else:
        form = ContactForm()
    
    return render(request, 'main_app/contact.html', {'form': form})

def experience(request):
    # Get work experiences
    work_experiences = Experience.objects.all().annotate(
        date=F('start_date'),
        type=models.Value('work', output_field=models.CharField())
    )
    
    # Get education 
    education = Education.objects.all().annotate(
        date=F('graduation_date'),
        type=models.Value('education', output_field=models.CharField())
    )
    
    # Combine both querysets and sort by date
    combined_experiences = sorted(
        chain(work_experiences, education),
        key=lambda x: x.date,
        reverse=True  # Most recent first
    )
    
    context = {
        'experiences': combined_experiences,
    }
    
    return render(request, 'main_app/experience.html', context)

def achievements(request):
    # Get all achievements ordered by date
    achievements_list = Achievement.objects.all()
    
    # Group achievements by category
    grouped_achievements = {
        'awards': achievements_list.filter(category='award'),
        'certifications': achievements_list.filter(category='certification'),
        'recognitions': achievements_list.filter(category='recognition'),
        'publications': achievements_list.filter(category='publication'),
    }
    
    # Remove empty categories
    grouped_achievements = {k: v for k, v in grouped_achievements.items() if v.exists()}
    
    context = {
        'grouped_achievements': grouped_achievements,
        'featured_achievements': achievements_list.filter(is_featured=True)[:3]
    }
    
    return render(request, 'main_app/achievements.html', context)



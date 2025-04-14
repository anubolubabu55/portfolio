# main_app/models.py
from django.db import models

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    CATEGORY_CHOICES = (("BACKEND", "Backend"),("FRONTEND", "Frontend"),("DATABASE", "Database"),
                        ("TOOLS", "Tools"),("VERSION_CONTROL", "Version"),("LIBRARIES", "Library"),("OTHER_TOOLS", "Other"))
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="BACKEND")
    description = models.TextField(blank=True)
    proficiency_level = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES)
    years_experience = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['category', '-proficiency_level']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=100)
    technology_used = models.CharField(max_length=200)
    technologies = models.ManyToManyField('Skill', blank=True, related_name='projects')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order       = models.IntegerField()
    date_completed = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-date_completed']
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Experiences'
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
    @property
    def is_current(self):
        return self.end_date is None

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    graduation_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-graduation_date']
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    has_been_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_sent']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    testimonial = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_displayed = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return f"{self.name} from {self.company}"

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('award', 'Award'),
        ('certification', 'Certification'),
        ('recognition', 'Recognition'),
        ('publication', 'Publication'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='award')
    organization = models.CharField(max_length=200)
    date_received = models.DateField()
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="Link to certificate or award details")
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_received']
        
    def __str__(self):
        return self.title

    
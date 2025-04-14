from django.contrib import admin
from .models import Project, Skill, Experience, Education, ContactMessage, Testimonial,Contact, Achievement

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_completed', 'is_featured', 'technology_used')
    list_filter = ('category', 'is_featured', 'date_completed', 'technology_used')
    search_fields = ('title', 'description', 'technology_used')
    date_hierarchy = 'date_completed'
    ordering = ('-date_completed',)
    filter_horizontal = ('technologies',)  # If you have a ManyToMany relationship
    prepopulated_fields = {'slug': ('title',)}  # If you have a slug field
    
    # Fieldsets for organized form layout in admin
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'description', 'image', 'category')
        }),
        ('Technical Details', {
            'fields': ('technology_used', 'technologies', 'github_url', 'live_url')
        }),
        ('Status', {
            'fields': ('is_featured', 'date_completed')
        }),
    )

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_level', 'years_experience')
    list_filter = ('category', 'proficiency_level')
    search_fields = ('name', 'description')
    list_editable = ('proficiency_level',)
    ordering = ('category', '-proficiency_level')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'location', 'start_date', 'end_date', 'is_current_job')
    list_filter = ('company',)  # Removed 'is_current' from list_filter
    search_fields = ('job_title', 'company', 'description', 'responsibilities')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    
    def is_current_job(self, obj):
        return obj.end_date is None
    is_current_job.boolean = True
    is_current_job.short_description = 'Current Job'

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'graduation_date')
    list_filter = ('degree',)
    search_fields = ('institution', 'field_of_study', 'description')
    date_hierarchy = 'graduation_date'
    ordering = ('-graduation_date',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'has_been_read')
    list_filter = ('date_sent', 'has_been_read')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'date_sent'
    readonly_fields = ('name', 'email', 'subject', 'message', 'date_sent')
    
    # You cannot edit a message once received
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
    # Action to mark messages as read
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(has_been_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'date_added', 'is_displayed')
    list_filter = ('is_displayed', 'company')
    search_fields = ('name', 'company', 'testimonial')
    list_editable = ('is_displayed',)
    ordering = ('-date_added',)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'organization', 'date_received', 'is_featured')
    list_filter = ('category', 'is_featured', 'organization')
    search_fields = ('title', 'description', 'organization')
    date_hierarchy = 'date_received'
    

# Register models with admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact)
admin.site.register(Achievement, AchievementAdmin)

# Custom admin site configuration
admin.site.site_header = "Anubolu Babu Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Admin Portal"

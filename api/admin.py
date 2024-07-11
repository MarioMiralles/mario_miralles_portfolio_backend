# Admin
# api/admin.py

from django.contrib import admin
from .models import Project, ContactMessage, Image

class ImageInline(admin.TabularInline):
    model = Project.images.through
    extra = 5  # Adjust the number of extra image fields as needed

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title', 'description', 'link')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage)
admin.site.register(Image)
from django.contrib import admin

from .models import Module, Lesson


class ContentAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'description', 'course_image', 'course_video', 'text_material')
    search_fields = ('title', 'description', 'user__username')
    
    

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module_number', 'module_title')  # Fields to display in the list view
    search_fields = ('module_number',)  # Enable search by module name
    list_filter = ('module_number',)  # Add filters for module name
    ordering = ('module_number',)  # Default ordering

# Register the Lesson model
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order', 'completed')  # Fields to display in the list view
    list_filter = ('module', 'completed')  # Add filters for module and completion status
    search_fields = ('title', 'description')  # Enable search by title and description
    ordering = ('order',)  # Default ordering by lesson order
    raw_id_fields = ('module',)  # Use a raw ID field for the module foreign key

    # Customize the form for adding/editing lessons
    fieldsets = (
        (None, {
            'fields': ('module', 'title', 'description', 'content', 'video', 'order', 'completed')
        }),
    )
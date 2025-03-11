from django.contrib import admin
from .models import UpdateCourse


class UpdateCourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'description', 'course_image', 'course_video', 'text_material')
    search_fields = ('title', 'description', 'user__username')
    
    
# Register your models here.
admin.site.register(UpdateCourse, UpdateCourseAdmin)
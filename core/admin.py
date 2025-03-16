from django.contrib import admin



class ContentAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'description', 'course_image', 'course_video', 'text_material')
    search_fields = ('title', 'description', 'user__username')
    
    
# Register your models here.
# admin.site.register(Content, ContentAdmin)
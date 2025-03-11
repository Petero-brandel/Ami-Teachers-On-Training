from django.db import models

# Create your models here.


class UpdateCourse(models.Model):
    course_title = models.CharField(max_length=100)
    description = models.TextField()
    text_material = models.TextField()
    course_image = models.ImageField(upload_to='course_images', null=True, blank=True)
    course_video = models.FileField(upload_to='course_videos', null=True, blank=True)
    course_created = models.DateTimeField(auto_now_add=True)
    course_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.course_title
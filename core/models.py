from django.db import models

class Module(models.Model):
    module_title = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.module_title

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons', default=0)
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.CharField(max_length=250, blank=True)
    content = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False) 
    

    
    def __str__(self):
        return self.title

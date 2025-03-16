from django.db import models

class Module(models.Model):
    module_name = models.CharField(max_length=100)
    module_description = models.TextField()
    
    def __str__(self):
        return self.module_name
    

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=250)
    description = models.CharField
    content = models.TextField()
    video = models.FloatField
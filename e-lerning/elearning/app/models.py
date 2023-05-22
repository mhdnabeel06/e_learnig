from django.db import models
from django.contrib import admin
# Create your models here.
class Course(models.Model):
    course_image=models.ImageField(upload_to='photos/courses')
    course_title=models.CharField(max_length=200)
    course_text=models.TextField(max_length=1000)
   
 
    
    def _str_(self):
        return self.course_title
    


class Topic(models.Model):
    name = models.CharField(max_length=225) 
    description = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='topics')
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='videos/',null=True,blank=True)

    def __str__(self):
        return self.name  
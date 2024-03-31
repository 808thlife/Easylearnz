from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length= 64)

    def __str__(self):
        return self.title

class Course(models.Model):

    COURSE_CATEGORY_CHOICES = {
        "A1": "Beginner",
        "B1": "Intermediate",
        "C1": "Advanced"
    }

    COURSE_CATEGORY_CHOICES = {
        "txt": "Text Based",
        "vd" : "Video Based"
    }

    title = models.CharField(max_length=132)
    description = models.TextField(max_length= 4048)
    difficulty = models.CharField(max_length=24)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default= 0)
    img = models.ImageField(upload_to = "courses/")
    wishlisted = models.IntegerField(default = 0) # indicates how many users wantto compelte this course
    participants = models.IntegerField(default=0)
    type = models.CharField(choices= COURSE_CATEGORY_CHOICES, default= "vd", max_length=24)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length= 1024)
    text_content = CKEditor5Field("Text Content", config_name= 'extends', blank=True)
    video_content = models.FileField(upload_to = "courses/videos", blank=True)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.title} from {self.course}"
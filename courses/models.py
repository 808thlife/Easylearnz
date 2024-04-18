from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length= 64)

    def __str__(self):
        return self.title
    
class Language(models.Model):
    title = models.CharField(_("Name of the lang"), max_length=50)

    def __str__(self):
        return self.title

class Course(models.Model):

    COURSE_DIFFICULTY_CHOICES = {
        "Beginner": "Beginner",
        "Intermediate": "Intermediate",
        "Advanced": "Advanced"
    }

    COURSE_CATEGORY_CHOICES = {
        "Text Based": "Text Based",
        "Video Based" : "Video Based"
    }
    
    slug = models.SlugField(_("Slug"))
    title = models.CharField(max_length=132) 
    description = CKEditor5Field("Text Content", config_name= 'extends') 
    difficulty = models.CharField(max_length=24, choices = COURSE_DIFFICULTY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default= 0)
    img = models.ImageField(upload_to = "courses/")
    wishlisted = models.IntegerField(default = 0) # indicates how many users wantto compelte this course
    participants = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    language = models.ForeignKey(Language, verbose_name=_("Language"), on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length= 1024)
    order = models.IntegerField(default=0)
    text_content = CKEditor5Field("Text Content", config_name= 'extends', blank=True)
    video_content = models.FileField(upload_to = "courses/videos", blank=True)
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE, blank= True, default=None, related_name="course")

    def __str__(self):
        return f"{self.title}"

    def __nonzero__(self):
        return bool(self.video_content)
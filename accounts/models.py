from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course

class User(AbstractUser):
    email = models.EmailField(max_length=64, unique=True)
    courses = models.ManyToManyField(Course, blank=True)
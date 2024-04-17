from django.contrib import admin

from .models import Course, Lesson, Category, Language

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Language)
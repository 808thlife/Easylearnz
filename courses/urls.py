from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.index, name = "index"),
    path("users/<int:ID>", views.profile_view, name = "user_profile"),
    path("course/<slug:slug>", views.course_view, name  = "course_view"),
    path("course/enroll/<int:ID>", views.course_enroll, name ="course_enroll"),
    path("course/lessons/<int:ID>", views.course_lessons, name = "course_lessons_view"),
    path("course/lesson/<int:ID>", views.lesson_view, name = "text_lesson_view")
]